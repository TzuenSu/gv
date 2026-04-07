#!/usr/bin/env python3
"""Compare BDD, FDD, and *BMD node counts on arithmetic functions."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


NOTE_DIR = Path(__file__).resolve().parents[1]
RESULT_DIR = NOTE_DIR / "results"
FIGURE_DIR = NOTE_DIR / "figures"


def bits_of(value: int, width: int) -> list[int]:
    return [(value >> i) & 1 for i in range(width)]


def assignments(nvars: int):
    for mask in range(1 << nvars):
        yield bits_of(mask, nvars)


def split_truth(
    values: tuple[int, ...], masks: tuple[int, ...], var: int
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    low: list[int] = []
    high: list[int] = []
    low_masks: list[int] = []
    high_masks: list[int] = []
    for mask, value in zip(masks, values):
        if (mask >> var) & 1:
            high.append(value)
            high_masks.append(mask)
        else:
            low.append(value)
            low_masks.append(mask)
    return tuple(low), tuple(high), tuple(low_masks), tuple(high_masks)


@dataclass(frozen=True)
class Node:
    kind: str
    var: int
    lo: int
    hi: int


class DecisionDiagram:
    """Reduced ordered DD manager.

    For BDD, nodes encode Shannon expansion:
      f = if x then hi else lo

    For pFDD, nodes encode positive Davio expansion:
      f = lo xor x * hi, where lo=f0 and hi=f0 xor f1

    For nFDD, nodes encode negative Davio expansion:
      f = lo xor (1 xor x) * hi, where lo=f1 and hi=f0 xor f1

    For BMD, nodes encode integer moment expansion:
      f = lo + x * hi, where lo=f0 and hi=f1-f0
    """

    def __init__(self, mode: str, nvars: int, order: tuple[int, ...]):
        self.mode = mode
        self.nvars = nvars
        self.order = order
        self.nodes: list[Node] = []
        self.unique: dict[Node, int] = {}
        self.terminals: dict[int, int] = {}
        self.memo: dict[tuple[int, tuple[int, ...], tuple[int, ...]], int] = {}

    def terminal(self, value: int) -> int:
        if value not in self.terminals:
            self.terminals[value] = -(len(self.terminals) + 1)
        return self.terminals[value]

    def mk(self, var: int, lo: int, hi: int) -> int:
        if hi == self.terminal(0):
            return lo
        node = Node(self.mode, var, lo, hi)
        if node not in self.unique:
            self.unique[node] = len(self.nodes)
            self.nodes.append(node)
        return self.unique[node]

    def build(self, truth: tuple[int, ...], masks: tuple[int, ...] | None = None, depth: int = 0) -> int:
        if masks is None:
            masks = tuple(range(len(truth)))
        key = (depth, truth, masks)
        if key in self.memo:
            return self.memo[key]
        if len(set(truth)) == 1:
            ret = self.terminal(truth[0])
        else:
            if depth >= len(self.order):
                raise ValueError("non-constant function with no variables left")
            var = self.order[depth]
            f0, f1, m0, m1 = split_truth(truth, masks, var)
            if self.mode == "bdd":
                lo = self.build(f0, m0, depth + 1)
                hi = self.build(f1, m1, depth + 1)
                if lo == hi:
                    ret = lo
                else:
                    ret = self.mk(var, lo, hi)
            elif self.mode == "pfdd":
                lo = self.build(f0, m0, depth + 1)
                derivative = tuple(a ^ b for a, b in zip(f0, f1))
                hi = self.build(derivative, m0, depth + 1)
                ret = self.mk(var, lo, hi)
            elif self.mode == "nfdd":
                lo = self.build(f1, m1, depth + 1)
                derivative = tuple(a ^ b for a, b in zip(f0, f1))
                hi = self.build(derivative, m0, depth + 1)
                ret = self.mk(var, lo, hi)
            elif self.mode == "bmd":
                lo = self.build(f0, m0, depth + 1)
                diff = tuple(b - a for a, b in zip(f0, f1))
                hi = self.build(diff, m0, depth + 1)
                ret = self.mk(var, lo, hi)
            else:
                raise ValueError(f"unknown mode: {self.mode}")
        self.memo[key] = ret
        return ret

    def node_count(self) -> int:
        return len(self.nodes)

    def terminal_count(self) -> int:
        return len(self.terminals)

    def write_dot(self, root: int, names: list[str], path: Path, title: str) -> None:
        def label(idx: int) -> str:
            if idx < 0:
                for value, tid in self.terminals.items():
                    if tid == idx:
                        return str(value)
            return names[self.nodes[idx].var]

        lines = ["digraph DD {", "  rankdir=TB;", f'  labelloc="t";', f'  label="{title}";']
        seen: set[int] = set()

        def emit(idx: int) -> None:
            if idx in seen:
                return
            seen.add(idx)
            if idx < 0:
                lines.append(f'  t{-idx} [shape=box,label="{label(idx)}"];')
                return
            node = self.nodes[idx]
            edge_label = {"bdd": ("0", "1"), "pfdd": ("f0", "d"), "nfdd": ("f1", "d"), "bmd": ("base", "coef")}[
                self.mode
            ]
            lines.append(f'  n{idx} [shape=circle,label="{label(idx)}"];')
            for child in (node.lo, node.hi):
                emit(child)
            lo_name = f"t{-node.lo}" if node.lo < 0 else f"n{node.lo}"
            hi_name = f"t{-node.hi}" if node.hi < 0 else f"n{node.hi}"
            lines.append(f'  n{idx} -> {lo_name} [style=dotted,label="{edge_label[0]}"];')
            lines.append(f'  n{idx} -> {hi_name} [label="{edge_label[1]}"];')

        emit(root)
        lines.append("}")
        path.write_text("\n".join(lines))


def var_names(nbits: int) -> list[str]:
    return [f"a[{i}]" for i in range(nbits)] + [f"b[{i}]" for i in range(nbits)]


def orders(nbits: int) -> dict[str, tuple[int, ...]]:
    file_order = tuple(range(2 * nbits))
    interleaved: list[int] = []
    for i in range(nbits):
        interleaved.extend([i, nbits + i])
    return {
        "file": file_order,
        "interleaved": tuple(interleaved),
    }


def operands(bits: list[int], nbits: int) -> tuple[int, int]:
    a = sum(bits[i] << i for i in range(nbits))
    b = sum(bits[nbits + i] << i for i in range(nbits))
    return a, b


def int_truth(nbits: int, func: str) -> tuple[int, ...]:
    vals: list[int] = []
    for bits in assignments(2 * nbits):
        a, b = operands(bits, nbits)
        if func == "add":
            vals.append(a + b)
        elif func == "mul":
            vals.append(a * b)
        elif func == "xor":
            vals.append(a ^ b)
        elif func == "dot2":
            low = (a & 0b11) * (b & 0b11)
            high = ((a >> 2) & 0b11) * ((b >> 2) & 0b11)
            vals.append(low + high)
        else:
            raise ValueError(func)
    return tuple(vals)


def bit_truth(values: tuple[int, ...], bit: int) -> tuple[int, ...]:
    return tuple((v >> bit) & 1 for v in values)


def run_bitwise_dd(nbits: int, func: str, mode: str, order_name: str, order: tuple[int, ...]) -> dict[str, int | str]:
    values = int_truth(nbits, func)
    width = max(values).bit_length() or 1
    total_nodes = 0
    max_nodes = 0
    sizes: list[int] = []
    for bit in range(width):
        mgr = DecisionDiagram(mode, 2 * nbits, order)
        root = mgr.build(bit_truth(values, bit))
        count = mgr.node_count()
        total_nodes += count
        max_nodes = max(max_nodes, count)
        sizes.append(count)
        if nbits == 4 and func in {"add", "mul"} and bit in {0, width - 1}:
            mgr.write_dot(root, var_names(nbits), FIGURE_DIR / f"{func}_{nbits}_{mode}_{order_name}_bit{bit}.dot", f"{func}_{nbits} {mode} {order_name} bit {bit}")
    return {
        "family": "bitwise_boolean",
        "function": func,
        "bits": nbits,
        "dd": mode,
        "order": order_name,
        "outputs": width,
        "total_nodes": total_nodes,
        "max_output_nodes": max_nodes,
        "per_output_nodes": " ".join(str(x) for x in sizes),
    }


def run_bmd(nbits: int, func: str, order_name: str, order: tuple[int, ...]) -> dict[str, int | str]:
    mgr = DecisionDiagram("bmd", 2 * nbits, order)
    root = mgr.build(int_truth(nbits, func))
    if nbits <= 4:
        mgr.write_dot(root, var_names(nbits), FIGURE_DIR / f"{func}_{nbits}_bmd_{order_name}.dot", f"{func}_{nbits} *BMD {order_name}")
    return {
        "family": "integer",
        "function": func,
        "bits": nbits,
        "dd": "bmd",
        "order": order_name,
        "outputs": 1,
        "total_nodes": mgr.node_count(),
        "max_output_nodes": mgr.node_count(),
        "per_output_nodes": str(mgr.node_count()),
    }


def write_report(rows: list[dict[str, int | str]]) -> None:
    def select(func: str, nbits: int, family: str = ""):
        return [
            r
            for r in rows
            if r["function"] == func and r["bits"] == nbits and (not family or r["family"] == family)
        ]

    lines = [
        "# result/25_LN Playing With Different DDs",
        "",
        "This note compares reduced ordered BDDs, Davio-style FDDs, and *BMDs on small arithmetic functions.",
        "",
        "Definitions used in the script:",
        "",
        "- BDD: Shannon expansion `f = if x then f1 else f0`.",
        "- positive FDD: positive Davio expansion `f = f0 xor x * (f0 xor f1)`.",
        "- negative FDD: negative Davio expansion `f = f1 xor (1 xor x) * (f0 xor f1)`.",
        "- *BMD: integer moment expansion `f = f0 + x * (f1 - f0)`.",
        "",
        "## Summary",
        "",
    ]
    for func in ["add", "mul", "xor", "dot2"]:
        lines.append(f"### {func}")
        lines.append("")
        lines.append("| bits | DD | order | total nodes | max output nodes | per-output nodes |")
        lines.append("|---:|---|---|---:|---:|---|")
        for nbits in [2, 3, 4, 5]:
            for r in select(func, nbits):
                lines.append(
                    f"| {r['bits']} | {r['dd']} | {r['order']} | {r['total_nodes']} | {r['max_output_nodes']} | `{r['per_output_nodes']}` |"
                )
        lines.append("")

    lines += [
        "## Conclusions",
        "",
        "- For addition, bit-interleaving keeps related variables adjacent and shrinks bitwise Boolean DDs.",
        "- For multiplication, bitwise BDD/FDD sizes grow quickly because middle product bits depend on many partial products.",
        "- *BMD is dramatically compact for arithmetic functions such as addition and multiplication because it stores integer polynomial structure directly instead of one Boolean output bit at a time.",
        "- FDD/Davio expansions help when XOR-like algebraic structure dominates. For pure XOR, FDD is small; for multiplication, it does not consistently beat BDD.",
        "- A practical heuristic is: use BDD/FDD for Boolean control or XOR-heavy logic, but use *BMD-like algebraic DDs for word-level arithmetic when the operation is naturally polynomial.",
        "",
        "Machine-readable data: `results/dd_summary.csv`.",
        "",
        "Selected DOT figures are in `figures/`. Convert one to PNG with `dot -Tpng <file.dot> -o <file.png>`.",
        "",
        "References:",
        "",
        "- R. E. Bryant, [`Graph-Based Algorithms for Boolean Function Manipulation`](https://www.cs.cmu.edu/~bryant/pubs.html), IEEE TC, 1986.",
        "- R. E. Bryant and Y.-A. Chen, [`Verification of Arithmetic Circuits with Binary Moment Diagrams`](https://www.cs.cmu.edu/~bryant/pubdir/dac95a.pdf), DAC 1995.",
        "- R. Drechsler and B. Becker, `Binary Decision Diagrams: Theory and Implementation`, 1998.",
    ]
    (NOTE_DIR / "README.md").write_text("\n".join(lines))


def main() -> int:
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, int | str]] = []
    for nbits in [2, 3, 4, 5]:
        for func in ["add", "mul", "xor"]:
            for order_name, order in orders(nbits).items():
                for mode in ["bdd", "pfdd", "nfdd"]:
                    rows.append(run_bitwise_dd(nbits, func, mode, order_name, order))
                rows.append(run_bmd(nbits, func, order_name, order))
        if nbits >= 4:
            for order_name, order in orders(nbits).items():
                for mode in ["bdd", "pfdd", "nfdd"]:
                    rows.append(run_bitwise_dd(nbits, "dot2", mode, order_name, order))
                rows.append(run_bmd(nbits, "dot2", order_name, order))

    csv_path = RESULT_DIR / "dd_summary.csv"
    fieldnames = ["family", "function", "bits", "dd", "order", "outputs", "total_nodes", "max_output_nodes", "per_output_nodes"]
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    write_report(rows)
    print(f"Wrote {csv_path}")
    print(f"Wrote {NOTE_DIR / 'README.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
