# result/25_LN Playing With Different DDs

This note compares reduced ordered BDDs, Davio-style FDDs, and *BMDs on small arithmetic functions.

Definitions used in the script:

- BDD: Shannon expansion `f = if x then f1 else f0`.
- positive FDD: positive Davio expansion `f = f0 xor x * (f0 xor f1)`.
- negative FDD: negative Davio expansion `f = f1 xor (1 xor x) * (f0 xor f1)`.
- *BMD: integer moment expansion `f = f0 + x * (f1 - f0)`.

## Summary

### add

| bits | DD | order | total nodes | max output nodes | per-output nodes |
|---:|---|---|---:|---:|---|
| 2 | bdd | file | 14 | 6 | `2 6 6` |
| 2 | pfdd | file | 12 | 6 | `2 4 6` |
| 2 | nfdd | file | 15 | 8 | `2 5 8` |
| 2 | bmd | file | 4 | 4 | `4` |
| 2 | bdd | interleaved | 12 | 5 | `2 5 5` |
| 2 | pfdd | interleaved | 11 | 5 | `2 4 5` |
| 2 | nfdd | interleaved | 13 | 6 | `2 5 6` |
| 2 | bmd | interleaved | 4 | 4 | `4` |
| 3 | bdd | file | 36 | 14 | `2 6 14 14` |
| 3 | pfdd | file | 28 | 14 | `2 4 8 14` |
| 3 | nfdd | file | 35 | 18 | `2 5 10 18` |
| 3 | bmd | file | 6 | 6 | `6` |
| 3 | bdd | interleaved | 23 | 8 | `2 5 8 8` |
| 3 | pfdd | interleaved | 21 | 8 | `2 4 7 8` |
| 3 | nfdd | interleaved | 24 | 9 | `2 5 8 9` |
| 3 | bmd | interleaved | 6 | 6 | `6` |
| 4 | bdd | file | 82 | 30 | `2 6 14 30 30` |
| 4 | pfdd | file | 60 | 30 | `2 4 8 16 30` |
| 4 | nfdd | file | 75 | 38 | `2 5 10 20 38` |
| 4 | bmd | file | 8 | 8 | `8` |
| 4 | bdd | interleaved | 37 | 11 | `2 5 8 11 11` |
| 4 | pfdd | interleaved | 34 | 11 | `2 4 7 10 11` |
| 4 | nfdd | interleaved | 38 | 12 | `2 5 8 11 12` |
| 4 | bmd | interleaved | 8 | 8 | `8` |
| 5 | bdd | file | 176 | 62 | `2 6 14 30 62 62` |
| 5 | pfdd | file | 124 | 62 | `2 4 8 16 32 62` |
| 5 | nfdd | file | 155 | 78 | `2 5 10 20 40 78` |
| 5 | bmd | file | 10 | 10 | `10` |
| 5 | bdd | interleaved | 54 | 14 | `2 5 8 11 14 14` |
| 5 | pfdd | interleaved | 50 | 14 | `2 4 7 10 13 14` |
| 5 | nfdd | interleaved | 55 | 15 | `2 5 8 11 14 15` |
| 5 | bmd | interleaved | 10 | 10 | `10` |

### mul

| bits | DD | order | total nodes | max output nodes | per-output nodes |
|---:|---|---|---:|---:|---|
| 2 | bdd | file | 14 | 6 | `2 6 2 4` |
| 2 | pfdd | file | 15 | 5 | `2 4 5 4` |
| 2 | nfdd | file | 18 | 6 | `2 6 6 4` |
| 2 | bmd | file | 6 | 6 | `6` |
| 2 | bdd | interleaved | 14 | 6 | `2 6 2 4` |
| 2 | pfdd | interleaved | 14 | 4 | `2 4 4 4` |
| 2 | nfdd | interleaved | 17 | 6 | `2 6 5 4` |
| 2 | bmd | interleaved | 7 | 7 | `7` |
| 3 | bdd | file | 58 | 15 | `2 6 15 13 12 10` |
| 3 | pfdd | file | 54 | 15 | `2 4 8 15 15 10` |
| 3 | nfdd | file | 77 | 22 | `2 6 13 21 22 13` |
| 3 | bmd | file | 12 | 12 | `12` |
| 3 | bdd | interleaved | 56 | 16 | `2 6 12 16 13 7` |
| 3 | pfdd | interleaved | 51 | 16 | `2 4 7 15 16 7` |
| 3 | nfdd | interleaved | 72 | 22 | `2 6 12 22 22 8` |
| 3 | bmd | interleaved | 14 | 14 | `14` |
| 4 | bdd | file | 194 | 42 | `2 6 15 38 41 42 29 21` |
| 4 | pfdd | file | 184 | 43 | `2 4 8 18 37 43 43 29` |
| 4 | nfdd | file | 241 | 67 | `2 6 13 25 48 67 53 27` |
| 4 | bmd | file | 20 | 20 | `20` |
| 4 | bdd | interleaved | 183 | 44 | `2 6 12 31 42 44 31 15` |
| 4 | pfdd | interleaved | 174 | 46 | `2 4 7 17 36 45 46 17` |
| 4 | nfdd | interleaved | 231 | 68 | `2 6 12 27 55 68 44 17` |
| 4 | bmd | interleaved | 23 | 23 | `23` |
| 5 | bdd | file | 588 | 121 | `2 6 15 38 93 115 121 96 58 44` |
| 5 | pfdd | file | 613 | 142 | `2 4 8 18 40 88 131 142 114 66` |
| 5 | nfdd | file | 826 | 197 | `2 6 13 25 52 129 194 197 146 62` |
| 5 | bmd | file | 30 | 30 | `30` |
| 5 | bdd | interleaved | 556 | 127 | `2 6 12 31 67 115 127 105 64 27` |
| 5 | pfdd | interleaved | 585 | 148 | `2 4 7 17 38 83 135 148 116 35` |
| 5 | nfdd | interleaved | 791 | 208 | `2 6 12 27 60 132 208 196 114 34` |
| 5 | bmd | interleaved | 34 | 34 | `34` |

### xor

| bits | DD | order | total nodes | max output nodes | per-output nodes |
|---:|---|---|---:|---:|---|
| 2 | bdd | file | 4 | 2 | `2 2` |
| 2 | pfdd | file | 4 | 2 | `2 2` |
| 2 | nfdd | file | 4 | 2 | `2 2` |
| 2 | bmd | file | 6 | 6 | `6` |
| 2 | bdd | interleaved | 4 | 2 | `2 2` |
| 2 | pfdd | interleaved | 4 | 2 | `2 2` |
| 2 | nfdd | interleaved | 4 | 2 | `2 2` |
| 2 | bmd | interleaved | 6 | 6 | `6` |
| 3 | bdd | file | 6 | 2 | `2 2 2` |
| 3 | pfdd | file | 6 | 2 | `2 2 2` |
| 3 | nfdd | file | 6 | 2 | `2 2 2` |
| 3 | bmd | file | 9 | 9 | `9` |
| 3 | bdd | interleaved | 6 | 2 | `2 2 2` |
| 3 | pfdd | interleaved | 6 | 2 | `2 2 2` |
| 3 | nfdd | interleaved | 6 | 2 | `2 2 2` |
| 3 | bmd | interleaved | 9 | 9 | `9` |
| 4 | bdd | file | 8 | 2 | `2 2 2 2` |
| 4 | pfdd | file | 8 | 2 | `2 2 2 2` |
| 4 | nfdd | file | 8 | 2 | `2 2 2 2` |
| 4 | bmd | file | 12 | 12 | `12` |
| 4 | bdd | interleaved | 8 | 2 | `2 2 2 2` |
| 4 | pfdd | interleaved | 8 | 2 | `2 2 2 2` |
| 4 | nfdd | interleaved | 8 | 2 | `2 2 2 2` |
| 4 | bmd | interleaved | 12 | 12 | `12` |
| 5 | bdd | file | 10 | 2 | `2 2 2 2 2` |
| 5 | pfdd | file | 10 | 2 | `2 2 2 2 2` |
| 5 | nfdd | file | 10 | 2 | `2 2 2 2 2` |
| 5 | bmd | file | 15 | 15 | `15` |
| 5 | bdd | interleaved | 10 | 2 | `2 2 2 2 2` |
| 5 | pfdd | interleaved | 10 | 2 | `2 2 2 2 2` |
| 5 | nfdd | interleaved | 10 | 2 | `2 2 2 2 2` |
| 5 | bmd | interleaved | 15 | 15 | `15` |

### dot2

| bits | DD | order | total nodes | max output nodes | per-output nodes |
|---:|---|---|---:|---:|---|
| 4 | bdd | file | 122 | 39 | `6 36 39 33 8` |
| 4 | pfdd | file | 73 | 28 | `4 10 23 28 8` |
| 4 | nfdd | file | 126 | 53 | `6 17 42 53 8` |
| 4 | bmd | file | 12 | 12 | `12` |
| 4 | bdd | interleaved | 81 | 26 | `4 21 26 22 8` |
| 4 | pfdd | interleaved | 68 | 23 | `4 11 22 23 8` |
| 4 | nfdd | interleaved | 102 | 37 | `6 18 37 33 8` |
| 4 | bmd | interleaved | 14 | 14 | `14` |
| 5 | bdd | file | 122 | 39 | `6 36 39 33 8` |
| 5 | pfdd | file | 73 | 28 | `4 10 23 28 8` |
| 5 | nfdd | file | 126 | 53 | `6 17 42 53 8` |
| 5 | bmd | file | 12 | 12 | `12` |
| 5 | bdd | interleaved | 81 | 26 | `4 21 26 22 8` |
| 5 | pfdd | interleaved | 68 | 23 | `4 11 22 23 8` |
| 5 | nfdd | interleaved | 102 | 37 | `6 18 37 33 8` |
| 5 | bmd | interleaved | 14 | 14 | `14` |

## Conclusions

- For addition, bit-interleaving keeps related variables adjacent and shrinks bitwise Boolean DDs.
- For multiplication, bitwise BDD/FDD sizes grow quickly because middle product bits depend on many partial products.
- *BMD is dramatically compact for arithmetic functions such as addition and multiplication because it stores integer polynomial structure directly instead of one Boolean output bit at a time.
- FDD/Davio expansions help when XOR-like algebraic structure dominates. For pure XOR, FDD is small; for multiplication, it does not consistently beat BDD.
- A practical heuristic is: use BDD/FDD for Boolean control or XOR-heavy logic, but use *BMD-like algebraic DDs for word-level arithmetic when the operation is naturally polynomial.

Machine-readable data: `results/dd_summary.csv`.

Selected DOT figures are in `figures/`. Convert one to PNG with `dot -Tpng <file.dot> -o <file.png>`.

References:

- R. E. Bryant, [`Graph-Based Algorithms for Boolean Function Manipulation`](https://www.cs.cmu.edu/~bryant/pubs.html), IEEE TC, 1986.
- R. E. Bryant and Y.-A. Chen, [`Verification of Arithmetic Circuits with Binary Moment Diagrams`](https://www.cs.cmu.edu/~bryant/pubdir/dac95a.pdf), DAC 1995.
- R. Drechsler and B. Becker, `Binary Decision Diagrams: Theory and Implementation`, 1998.