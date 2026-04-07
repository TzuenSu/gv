# result/18_LN BDD Variable Ordering Results

This folder contains GV scripts, BDD reports, Graphviz dot files, and PNG drawings generated from `adder_4.v`, `mult_4.v`, `adder_8.v`, and `mult_8.v`.

Implemented GV command options: `BSETOrder -DFS` and `BSETOrder -RDFS`.

Orders:
- `file`: Verilog input declaration order.
- `dfs`: collect PI/current-state variables in post-order DFS from POs and FF inputs.
- `rdfs`: reverse of that DFS collection order.

## PO Lists

### adder_4

`POs of the circuit: 37 38 39 40 41`

### mult_4

`POs of the circuit: 97 98 99 100 101 102 103 104`

### adder_8

`POs of the circuit: 84 85 86 87 88 89 90 91 92`

### mult_8

`POs of the circuit: 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495`

## BDD Size Tables

### adder_4 / file

| PO | Gate | Name | BDD nodes | Status | PNG |
|---:|---:|---|---:|---|---|
| 0 | 37 | `sum[0]` | 3 | ok | [png](results/adder_4/file/adder_4_file_po00_sum_0.png) |
| 1 | 38 | `sum[1]` | 6 | ok | [png](results/adder_4/file/adder_4_file_po01_sum_1.png) |
| 2 | 39 | `sum[2]` | 13 | ok | [png](results/adder_4/file/adder_4_file_po02_sum_2.png) |
| 3 | 40 | `sum[3]` | 28 | ok | [png](results/adder_4/file/adder_4_file_po03_sum_3.png) |
| 4 | 41 | `cout[0]` | 42 | ok | [png](results/adder_4/file/adder_4_file_po04_cout_0.png) |

Fit: `bdd_size = 3.13 * 1.98^po_index`

### adder_4 / dfs

| PO | Gate | Name | BDD nodes | Status | PNG |
|---:|---:|---|---:|---|---|
| 0 | 37 | `sum[0]` | 3 | ok | [png](results/adder_4/dfs/adder_4_dfs_po00_sum_0.png) |
| 1 | 38 | `sum[1]` | 5 | ok | [png](results/adder_4/dfs/adder_4_dfs_po01_sum_1.png) |
| 2 | 39 | `sum[2]` | 8 | ok | [png](results/adder_4/dfs/adder_4_dfs_po02_sum_2.png) |
| 3 | 40 | `sum[3]` | 11 | ok | [png](results/adder_4/dfs/adder_4_dfs_po03_sum_3.png) |
| 4 | 41 | `cout[0]` | 12 | ok | [png](results/adder_4/dfs/adder_4_dfs_po04_cout_0.png) |

Fit: `bdd_size = 3.39 * 1.43^po_index`

### adder_4 / rdfs

| PO | Gate | Name | BDD nodes | Status | PNG |
|---:|---:|---|---:|---|---|
| 0 | 37 | `sum[0]` | 3 | ok | [png](results/adder_4/rdfs/adder_4_rdfs_po00_sum_0.png) |
| 1 | 38 | `sum[1]` | 5 | ok | [png](results/adder_4/rdfs/adder_4_rdfs_po01_sum_1.png) |
| 2 | 39 | `sum[2]` | 8 | ok | [png](results/adder_4/rdfs/adder_4_rdfs_po02_sum_2.png) |
| 3 | 40 | `sum[3]` | 11 | ok | [png](results/adder_4/rdfs/adder_4_rdfs_po03_sum_3.png) |
| 4 | 41 | `cout[0]` | 12 | ok | [png](results/adder_4/rdfs/adder_4_rdfs_po04_cout_0.png) |

Fit: `bdd_size = 3.39 * 1.43^po_index`

### mult_4 / file

| PO | Gate | Name | BDD nodes | Status | PNG |
|---:|---:|---|---:|---|---|
| 0 | 97 | `p[0]` | 3 | ok | [png](results/mult_4/file/mult_4_file_po00_p_0.png) |
| 1 | 98 | `p[1]` | 7 | ok | [png](results/mult_4/file/mult_4_file_po01_p_1.png) |
| 2 | 99 | `p[2]` | 17 | ok | [png](results/mult_4/file/mult_4_file_po02_p_2.png) |
| 3 | 100 | `p[3]` | 41 | ok | [png](results/mult_4/file/mult_4_file_po03_p_3.png) |
| 4 | 101 | `p[4]` | 47 | ok | [png](results/mult_4/file/mult_4_file_po04_p_4.png) |
| 5 | 102 | `p[5]` | 46 | ok | [png](results/mult_4/file/mult_4_file_po05_p_5.png) |
| 6 | 103 | `p[6]` | 37 | ok | [png](results/mult_4/file/mult_4_file_po06_p_6.png) |
| 7 | 104 | `p[7]` | 25 | ok | [png](results/mult_4/file/mult_4_file_po07_p_7.png) |

Fit: `bdd_size = 6.80 * 1.37^po_index`

### mult_4 / dfs

| PO | Gate | Name | BDD nodes | Status | PNG |
|---:|---:|---|---:|---|---|
| 0 | 97 | `p[0]` | 3 | ok | [png](results/mult_4/dfs/mult_4_dfs_po00_p_0.png) |
| 1 | 98 | `p[1]` | 7 | ok | [png](results/mult_4/dfs/mult_4_dfs_po01_p_1.png) |
| 2 | 99 | `p[2]` | 19 | ok | [png](results/mult_4/dfs/mult_4_dfs_po02_p_2.png) |
| 3 | 100 | `p[3]` | 63 | ok | [png](results/mult_4/dfs/mult_4_dfs_po03_p_3.png) |
| 4 | 101 | `p[4]` | 50 | ok | [png](results/mult_4/dfs/mult_4_dfs_po04_p_4.png) |
| 5 | 102 | `p[5]` | 37 | ok | [png](results/mult_4/dfs/mult_4_dfs_po05_p_5.png) |
| 6 | 103 | `p[6]` | 28 | ok | [png](results/mult_4/dfs/mult_4_dfs_po06_p_6.png) |
| 7 | 104 | `p[7]` | 15 | ok | [png](results/mult_4/dfs/mult_4_dfs_po07_p_7.png) |

Fit: `bdd_size = 8.41 * 1.27^po_index`

### mult_4 / rdfs

| PO | Gate | Name | BDD nodes | Status | PNG |
|---:|---:|---|---:|---|---|
| 0 | 97 | `p[0]` | 3 | ok | [png](results/mult_4/rdfs/mult_4_rdfs_po00_p_0.png) |
| 1 | 98 | `p[1]` | 7 | ok | [png](results/mult_4/rdfs/mult_4_rdfs_po01_p_1.png) |
| 2 | 99 | `p[2]` | 13 | ok | [png](results/mult_4/rdfs/mult_4_rdfs_po02_p_2.png) |
| 3 | 100 | `p[3]` | 30 | ok | [png](results/mult_4/rdfs/mult_4_rdfs_po03_p_3.png) |
| 4 | 101 | `p[4]` | 48 | ok | [png](results/mult_4/rdfs/mult_4_rdfs_po04_p_4.png) |
| 5 | 102 | `p[5]` | 55 | ok | [png](results/mult_4/rdfs/mult_4_rdfs_po05_p_5.png) |
| 6 | 103 | `p[6]` | 40 | ok | [png](results/mult_4/rdfs/mult_4_rdfs_po06_p_6.png) |
| 7 | 104 | `p[7]` | 16 | ok | [png](results/mult_4/rdfs/mult_4_rdfs_po07_p_7.png) |

Fit: `bdd_size = 6.47 * 1.35^po_index`

### adder_8 / file

| PO | Gate | Name | BDD nodes | Status | PNG |
|---:|---:|---|---:|---|---|
| 0 | 84 | `sum[0]` | 3 | ok | [png](results/adder_8/file/adder_8_file_po00_sum_0.png) |
| 1 | 85 | `sum[1]` | 6 | ok | [png](results/adder_8/file/adder_8_file_po01_sum_1.png) |
| 2 | 86 | `sum[2]` | 13 | ok | [png](results/adder_8/file/adder_8_file_po02_sum_2.png) |
| 3 | 87 | `sum[3]` | 28 | ok | [png](results/adder_8/file/adder_8_file_po03_sum_3.png) |
| 4 | 88 | `sum[4]` | 59 | ok | [png](results/adder_8/file/adder_8_file_po04_sum_4.png) |
| 5 | 89 | `sum[5]` | 122 | ok | [png](results/adder_8/file/adder_8_file_po05_sum_5.png) |
| 6 | 90 | `sum[6]` | 249 | ok | [png](results/adder_8/file/adder_8_file_po06_sum_6.png) |
| 7 | 91 | `sum[7]` | 504 | ok | [png](results/adder_8/file/adder_8_file_po07_sum_7.png) |
| 8 | 92 | `cout[0]` | 758 | ok | [png](results/adder_8/file/adder_8_file_po08_cout_0.png) |

Fit: `bdd_size = 3.16 * 2.04^po_index`

### adder_8 / dfs

| PO | Gate | Name | BDD nodes | Status | PNG |
|---:|---:|---|---:|---|---|
| 0 | 84 | `sum[0]` | 3 | ok | [png](results/adder_8/dfs/adder_8_dfs_po00_sum_0.png) |
| 1 | 85 | `sum[1]` | 5 | ok | [png](results/adder_8/dfs/adder_8_dfs_po01_sum_1.png) |
| 2 | 86 | `sum[2]` | 8 | ok | [png](results/adder_8/dfs/adder_8_dfs_po02_sum_2.png) |
| 3 | 87 | `sum[3]` | 11 | ok | [png](results/adder_8/dfs/adder_8_dfs_po03_sum_3.png) |
| 4 | 88 | `sum[4]` | 14 | ok | [png](results/adder_8/dfs/adder_8_dfs_po04_sum_4.png) |
| 5 | 89 | `sum[5]` | 17 | ok | [png](results/adder_8/dfs/adder_8_dfs_po05_sum_5.png) |
| 6 | 90 | `sum[6]` | 20 | ok | [png](results/adder_8/dfs/adder_8_dfs_po06_sum_6.png) |
| 7 | 91 | `sum[7]` | 23 | ok | [png](results/adder_8/dfs/adder_8_dfs_po07_sum_7.png) |
| 8 | 92 | `cout[0]` | 24 | ok | [png](results/adder_8/dfs/adder_8_dfs_po08_cout_0.png) |

Fit: `bdd_size = 4.18 * 1.29^po_index`

### adder_8 / rdfs

| PO | Gate | Name | BDD nodes | Status | PNG |
|---:|---:|---|---:|---|---|
| 0 | 84 | `sum[0]` | 3 | ok | [png](results/adder_8/rdfs/adder_8_rdfs_po00_sum_0.png) |
| 1 | 85 | `sum[1]` | 5 | ok | [png](results/adder_8/rdfs/adder_8_rdfs_po01_sum_1.png) |
| 2 | 86 | `sum[2]` | 8 | ok | [png](results/adder_8/rdfs/adder_8_rdfs_po02_sum_2.png) |
| 3 | 87 | `sum[3]` | 11 | ok | [png](results/adder_8/rdfs/adder_8_rdfs_po03_sum_3.png) |
| 4 | 88 | `sum[4]` | 14 | ok | [png](results/adder_8/rdfs/adder_8_rdfs_po04_sum_4.png) |
| 5 | 89 | `sum[5]` | 17 | ok | [png](results/adder_8/rdfs/adder_8_rdfs_po05_sum_5.png) |
| 6 | 90 | `sum[6]` | 20 | ok | [png](results/adder_8/rdfs/adder_8_rdfs_po06_sum_6.png) |
| 7 | 91 | `sum[7]` | 23 | ok | [png](results/adder_8/rdfs/adder_8_rdfs_po07_sum_7.png) |
| 8 | 92 | `cout[0]` | 24 | ok | [png](results/adder_8/rdfs/adder_8_rdfs_po08_cout_0.png) |

Fit: `bdd_size = 4.18 * 1.29^po_index`

### mult_8 / file

| PO | Gate | Name | BDD nodes | Status | PNG |
|---:|---:|---|---:|---|---|
| 0 | 480 | `p[0]` | 3 | ok | [png](results/mult_8/file/mult_8_file_po00_p_0.png) |
| 1 | 481 | `p[1]` | 7 | ok | [png](results/mult_8/file/mult_8_file_po01_p_1.png) |
| 2 | 482 | `p[2]` | 17 | ok | [png](results/mult_8/file/mult_8_file_po02_p_2.png) |
| 3 | 483 | `p[3]` | 41 | ok | [png](results/mult_8/file/mult_8_file_po03_p_3.png) |
| 4 | 484 | `p[4]` | 101 | ok | [png](results/mult_8/file/mult_8_file_po04_p_4.png) |
| 5 | 485 | `p[5]` | 257 | ok | [png](results/mult_8/file/mult_8_file_po05_p_5.png) |
| 6 | 486 | `p[6]` | 635 | ok | [png](results/mult_8/file/mult_8_file_po06_p_6.png) |
| 7 | 487 | `p[7]` | 1645 | ok | [png](results/mult_8/file/mult_8_file_po07_p_7.png) |
| 8 | 488 | `p[8]` | 2915 | ok | [png](results/mult_8/file/mult_8_file_po08_p_8.png) |
| 9 | 489 | `p[9]` | 2870 | ok | [png](results/mult_8/file/mult_8_file_po09_p_9.png) |
| 10 | 490 | `p[10]` | 2492 | ok | [png](results/mult_8/file/mult_8_file_po10_p_10.png) |
| 11 | 491 | `p[11]` | 2027 | ok | [png](results/mult_8/file/mult_8_file_po11_p_11.png) |
| 12 | 492 | `p[12]` | 1554 | ok | [png](results/mult_8/file/mult_8_file_po12_p_12.png) |
| 13 | 493 | `p[13]` | 1026 | ok | [png](results/mult_8/file/mult_8_file_po13_p_13.png) |
| 14 | 494 | `p[14]` | 675 | ok | [png](results/mult_8/file/mult_8_file_po14_p_14.png) |
| 15 | 495 | `p[15]` | 453 | ok | [png](results/mult_8/file/mult_8_file_po15_p_15.png) |

Fit: `bdd_size = 2.85 * 2.46^po_index`

### mult_8 / dfs

| PO | Gate | Name | BDD nodes | Status | PNG |
|---:|---:|---|---:|---|---|
| 0 | 480 | `p[0]` | 3 | ok | [png](results/mult_8/dfs/mult_8_dfs_po00_p_0.png) |
| 1 | 481 | `p[1]` | 7 | ok | [png](results/mult_8/dfs/mult_8_dfs_po01_p_1.png) |
| 2 | 482 | `p[2]` | 19 | ok | [png](results/mult_8/dfs/mult_8_dfs_po02_p_2.png) |
| 3 | 483 | `p[3]` | 63 | ok | [png](results/mult_8/dfs/mult_8_dfs_po03_p_3.png) |
| 4 | 484 | `p[4]` | 183 | ok | [png](results/mult_8/dfs/mult_8_dfs_po04_p_4.png) |
| 5 | 485 | `p[5]` | 511 | ok | [png](results/mult_8/dfs/mult_8_dfs_po05_p_5.png) |
| 6 | 486 | `p[6]` | 1523 | ok | [png](results/mult_8/dfs/mult_8_dfs_po06_p_6.png) |
| 7 | 487 | `p[7]` | 4647 | ok | [png](results/mult_8/dfs/mult_8_dfs_po07_p_7.png) |
| 8 | 488 | `p[8]` | 3976 | ok | [png](results/mult_8/dfs/mult_8_dfs_po08_p_8.png) |
| 9 | 489 | `p[9]` | 3077 | ok | [png](results/mult_8/dfs/mult_8_dfs_po09_p_9.png) |
| 10 | 490 | `p[10]` | 2193 | ok | [png](results/mult_8/dfs/mult_8_dfs_po10_p_10.png) |
| 11 | 491 | `p[11]` | 1458 | ok | [png](results/mult_8/dfs/mult_8_dfs_po11_p_11.png) |
| 12 | 492 | `p[12]` | 1058 | ok | [png](results/mult_8/dfs/mult_8_dfs_po12_p_12.png) |
| 13 | 493 | `p[13]` | 655 | ok | [png](results/mult_8/dfs/mult_8_dfs_po13_p_13.png) |
| 14 | 494 | `p[14]` | 338 | ok | [png](results/mult_8/dfs/mult_8_dfs_po14_p_14.png) |
| 15 | 495 | `p[15]` | 135 | ok | [png](results/mult_8/dfs/mult_8_dfs_po15_p_15.png) |

Fit: `bdd_size = 2.58 * 2.89^po_index`

### mult_8 / rdfs

| PO | Gate | Name | BDD nodes | Status | PNG |
|---:|---:|---|---:|---|---|
| 0 | 480 | `p[0]` | 3 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po00_p_0.png) |
| 1 | 481 | `p[1]` | 7 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po01_p_1.png) |
| 2 | 482 | `p[2]` | 13 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po02_p_2.png) |
| 3 | 483 | `p[3]` | 30 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po03_p_3.png) |
| 4 | 484 | `p[4]` | 62 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po04_p_4.png) |
| 5 | 485 | `p[5]` | 144 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po05_p_5.png) |
| 6 | 486 | `p[6]` | 325 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po06_p_6.png) |
| 7 | 487 | `p[7]` | 777 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po07_p_7.png) |
| 8 | 488 | `p[8]` | 1775 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po08_p_8.png) |
| 9 | 489 | `p[9]` | 3537 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po09_p_9.png) |
| 10 | 490 | `p[10]` | 4419 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po10_p_10.png) |
| 11 | 491 | `p[11]` | 3872 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po11_p_11.png) |
| 12 | 492 | `p[12]` | 2362 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po12_p_12.png) |
| 13 | 493 | `p[13]` | 1165 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po13_p_13.png) |
| 14 | 494 | `p[14]` | 520 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po14_p_14.png) |
| 15 | 495 | `p[15]` | 167 | ok | [png](results/mult_8/rdfs/mult_8_rdfs_po15_p_15.png) |

Fit: `bdd_size = 2.91 * 2.19^po_index`

## Conclusions

- For ripple-carry adders, grouping variables by bit position, such as `a[0], b[0], a[1], b[1], ...`, is usually better than grouping all `a` bits before all `b` bits. The carry chain is local, so adjacent related inputs keep intermediate BDDs small.
- For multipliers, the low-order product bits depend on fewer partial products, while middle bits depend on many cross terms. Even a good order grows much faster near the middle outputs.
- DFS/RDFS orders are structural heuristics. They can help when the circuit topology naturally visits related inputs together, but they are not guaranteed to dominate a hand-made bit-interleaved order.
- A practical heuristic is to place variables that interact in the same local logic cone close together, then test both forward and reverse orders because complemented/reconvergent structure can make the reverse surprisingly different.

The full machine-readable table is `results/summary.csv`.
