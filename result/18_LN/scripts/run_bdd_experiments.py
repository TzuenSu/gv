#!/usr/bin/env python3
"""Run GV BDD variable-ordering experiments and collect results."""

from __future__ import annotations

import csv
import math
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ASSIGNMENT_DIR = Path(__file__).resolve().parents[1]
ROOT = ASSIGNMENT_DIR.parents[1]
DESIGN_DIR = ASSIGNMENT_DIR / "designs"
RESULT_DIR = ASSIGNMENT_DIR / "results"
GV = ROOT / "gv"

DESIGNS = ["adder_4", "mult_4", "adder_8", "mult_8"]
ORDERS = {
    "file": "-file",
    "dfs": "-dfs",
    "rdfs": "-rdfs",
}
TIMEOUT_SEC = 120


@dataclass
class PoInfo:
    index: int
    gate_id: int
    name: str


def run_gv(commands: list[str], timeout: int = TIMEOUT_SEC) -> subprocess.CompletedProcess[str]:
    script = "\n".join(commands + ["q -f", ""])
    return subprocess.run(
        [str(GV)],
        cwd=ROOT,
        input=script,
        text=True,
        capture_output=True,
        timeout=timeout,
    )


def inspect_design(design: str) -> tuple[list[PoInfo], str]:
    verilog = DESIGN_DIR / f"{design}.v"
    proc = run_gv([f"cirread -v {verilog}", "cirprint -po", "cirprint -net"])
    log = proc.stdout + proc.stderr
    if proc.returncode != 0:
        raise RuntimeError(f"GV failed while inspecting {design}:\n{log}")

    po_line = re.search(r"POs of the circuit:(.*)", log)
    if not po_line:
        raise RuntimeError(f"Cannot find PO list for {design}:\n{log}")
    po_ids = [int(x) for x in po_line.group(1).split()]

    names_by_gid: dict[int, str] = {}
    for match in re.finditer(r"\[\d+\]\s+PO\s+(\d+)\s+.*?\(([^)]*)\)", log):
        names_by_gid[int(match.group(1))] = match.group(2)

    pos = [
        PoInfo(index=i, gate_id=gid, name=names_by_gid.get(gid, f"po[{i}]"))
        for i, gid in enumerate(po_ids)
    ]
    return pos, log


def parse_bdd_size(report: Path) -> int | None:
    if not report.exists():
        return None
    match = re.search(r"Total #BddNodeVs\s*:\s*(\d+)", report.read_text())
    return int(match.group(1)) if match else None


def build_one(design: str, po: PoInfo, order_name: str, order_flag: str) -> dict[str, str | int]:
    out_dir = RESULT_DIR / design / order_name
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{design}_{order_name}_po{po.index:02d}_{po.name.replace('[', '_').replace(']', '')}"
    report = out_dir / f"{stem}.bdd.txt"
    dot = out_dir / f"{stem}.dot"
    png = out_dir / f"{stem}.png"
    log_path = out_dir / f"{stem}.log"
    dofile = out_dir / f"{stem}.do"

    commands = [
        f"cirread -v {DESIGN_DIR / (design + '.v')}",
        "breset 2000 8009 30011",
        f"bsetorder {order_flag}",
        f"bcons -output {po.index}",
        f"brep {po.gate_id} -file {report}",
        f"bdraw {po.gate_id} {dot}",
    ]
    dofile.write_text("\n".join(commands + ["q -f", ""]))

    status = "ok"
    try:
        proc = run_gv(commands)
        log_path.write_text(proc.stdout + proc.stderr)
        if proc.returncode != 0:
            status = f"gv_exit_{proc.returncode}"
    except subprocess.TimeoutExpired as exc:
        status = "timeout"
        log_path.write_text((exc.stdout or "") + (exc.stderr or ""))

    size = parse_bdd_size(report)
    if status == "ok" and size is None:
        status = "missing_report"

    if status == "ok" and dot.exists():
        dot_proc = subprocess.run(
            ["dot", "-Tpng", str(dot), "-o", str(png)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=TIMEOUT_SEC,
        )
        if dot_proc.returncode != 0:
            status = "dot_failed"
            log_path.write_text(log_path.read_text() + "\n[dot]\n" + dot_proc.stderr)

    return {
        "design": design,
        "order": order_name,
        "po_index": po.index,
        "po_gate_id": po.gate_id,
        "po_name": po.name,
        "bdd_size": size if size is not None else "",
        "status": status,
        "report": str(report.relative_to(ASSIGNMENT_DIR)),
        "dot": str(dot.relative_to(ASSIGNMENT_DIR)),
        "png": str(png.relative_to(ASSIGNMENT_DIR)) if png.exists() else "",
        "log": str(log_path.relative_to(ASSIGNMENT_DIR)),
        "dofile": str(dofile.relative_to(ASSIGNMENT_DIR)),
    }


def fit_exponential(rows: list[dict[str, str | int]]) -> tuple[float, float] | None:
    points = [
        (int(r["po_index"]), int(r["bdd_size"]))
        for r in rows
        if r["status"] == "ok" and str(r["bdd_size"]) != "" and int(r["bdd_size"]) > 0
    ]
    if len(points) < 2:
        return None
    n = len(points)
    sx = sum(x for x, _ in points)
    sy = sum(math.log(y) for _, y in points)
    sxx = sum(x * x for x, _ in points)
    sxy = sum(x * math.log(y) for x, y in points)
    denom = n * sxx - sx * sx
    if denom == 0:
        return None
    b_log = (n * sxy - sx * sy) / denom
    a_log = (sy - b_log * sx) / n
    return math.exp(a_log), math.exp(b_log)


def write_summary(rows: list[dict[str, str | int]], inspections: dict[str, str]) -> None:
    csv_path = RESULT_DIR / "summary.csv"
    fields = [
        "design",
        "order",
        "po_index",
        "po_gate_id",
        "po_name",
        "bdd_size",
        "status",
        "png",
        "report",
        "dot",
        "log",
        "dofile",
    ]
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# result/18_LN BDD Variable Ordering Results",
        "",
        "This folder contains GV scripts, BDD reports, Graphviz dot files, and PNG drawings generated from `adder_4.v`, `mult_4.v`, `adder_8.v`, and `mult_8.v`.",
        "",
        "Implemented GV command options: `BSETOrder -DFS` and `BSETOrder -RDFS`.",
        "",
        "Orders:",
        "- `file`: Verilog input declaration order.",
        "- `dfs`: collect PI/current-state variables in post-order DFS from POs and FF inputs.",
        "- `rdfs`: reverse of that DFS collection order.",
        "",
        "## PO Lists",
        "",
    ]
    for design, log in inspections.items():
        po_line = re.search(r"POs of the circuit:(.*)", log)
        lines.append(f"### {design}")
        lines.append("")
        lines.append(f"`{po_line.group(0).strip() if po_line else 'PO list not found'}`")
        lines.append("")

    lines += ["## BDD Size Tables", ""]
    for design in DESIGNS:
        for order in ORDERS:
            group = [r for r in rows if r["design"] == design and r["order"] == order]
            lines.append(f"### {design} / {order}")
            lines.append("")
            lines.append("| PO | Gate | Name | BDD nodes | Status | PNG |")
            lines.append("|---:|---:|---|---:|---|---|")
            for r in group:
                png = f"[png]({r['png']})" if r["png"] else ""
                lines.append(
                    f"| {r['po_index']} | {r['po_gate_id']} | `{r['po_name']}` | {r['bdd_size']} | {r['status']} | {png} |"
                )
            fit = fit_exponential(group[:8] if design.startswith("mult_8") else group)
            if fit:
                a, b = fit
                lines.append("")
                lines.append(f"Fit: `bdd_size = {a:.2f} * {b:.2f}^po_index`")
            lines.append("")

    lines += [
        "## Conclusions",
        "",
        "- For ripple-carry adders, grouping variables by bit position, such as `a[0], b[0], a[1], b[1], ...`, is usually better than grouping all `a` bits before all `b` bits. The carry chain is local, so adjacent related inputs keep intermediate BDDs small.",
        "- For multipliers, the low-order product bits depend on fewer partial products, while middle bits depend on many cross terms. Even a good order grows much faster near the middle outputs.",
        "- DFS/RDFS orders are structural heuristics. They can help when the circuit topology naturally visits related inputs together, but they are not guaranteed to dominate a hand-made bit-interleaved order.",
        "- A practical heuristic is to place variables that interact in the same local logic cone close together, then test both forward and reverse orders because complemented/reconvergent structure can make the reverse surprisingly different.",
        "",
        "The full machine-readable table is `results/summary.csv`.",
        "",
    ]
    (ASSIGNMENT_DIR / "README.md").write_text("\n".join(lines))


def main() -> int:
    if not GV.exists():
        print(f"Cannot find GV binary: {GV}", file=sys.stderr)
        return 1
    RESULT_DIR.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, str | int]] = []
    inspections: dict[str, str] = {}
    for design in DESIGNS:
        pos, log = inspect_design(design)
        inspections[design] = log
        (RESULT_DIR / design).mkdir(parents=True, exist_ok=True)
        (RESULT_DIR / design / "inspect.log").write_text(log)
        for order_name, order_flag in ORDERS.items():
            for po in pos:
                print(f"{design:8s} {order_name:4s} PO {po.index:02d} ({po.name})")
                rows.append(build_one(design, po, order_name, order_flag))

    write_summary(rows, inspections)
    print(f"\nWrote {RESULT_DIR / 'summary.csv'}")
    print(f"Wrote {ASSIGNMENT_DIR / 'README.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
