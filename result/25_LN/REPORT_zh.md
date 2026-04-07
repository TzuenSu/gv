# 3/25 LN：Playing with Different DDs

## 目標

這份 learning note 的目標是比較不同 decision diagrams 在 arithmetic functions 上的節點數變化。本次採用一個可重跑的 Python prototype，而不是直接把完整 FDD package 整合進 GV core。原因是這題重點是觀察不同 DD 的大小趨勢；standalone prototype 比較容易驗證，也不會讓 GV 原始碼變得太大。

本實驗比較：

- BDD：Shannon expansion，`f = if x then f1 else f0`
- positive FDD：positive Davio expansion，`f = f0 xor x * (f0 xor f1)`
- negative FDD：negative Davio expansion，`f = f1 xor (1 xor x) * (f0 xor f1)`
- *BMD：integer moment expansion，`f = f0 + x * (f1 - f0)`

## 檔案位置

- 實驗腳本：`result/25_LN/scripts/dd_compare.py`
- 完整 CSV 結果：`result/25_LN/results/dd_summary.csv`
- 英文版總表：`result/25_LN/README.md`
- 圖片與 DOT：`result/25_LN/figures/`

## 實驗設定

測試 functions：

- `add`: `a + b`
- `mul`: `a * b`
- `xor`: `a xor b`
- `dot2`: 兩個 2-bit partial products 的 sum，模擬小型 dot-product pattern

測試 bit-width：

- `add`, `mul`, `xor`: 2, 3, 4, 5 bits
- `dot2`: 4, 5 bits

Variable orders：

- `file`: `a[0], a[1], ..., b[0], b[1], ...`
- `interleaved`: `a[0], b[0], a[1], b[1], ...`

BDD/FDD 是 bitwise Boolean DD，所以一個 arithmetic output 的每個 output bit 各建一個 DD，再把節點數加總。*BMD 則直接表示 integer-valued function，因此一個 function 只建一個 word-level DD。

## 重要結果

### 5-bit addition, interleaved order

| DD | Total nodes | Per-output nodes |
|---|---:|---|
| BDD | 54 | `2 5 8 11 14 14` |
| pFDD | 50 | `2 4 7 10 13 14` |
| nFDD | 55 | `2 5 8 11 14 15` |
| *BMD | 10 | `10` |

Observation：bit-interleaving 對 adder 很有效，因為 carry propagation 是 bit-wise local。*BMD 又更小，因為它直接表示 `a + b` 的 integer polynomial structure。

### 5-bit multiplication, interleaved order

| DD | Total nodes | Per-output nodes |
|---|---:|---|
| BDD | 556 | `2 6 12 31 67 115 127 105 64 27` |
| pFDD | 585 | `2 4 7 17 38 83 135 148 116 35` |
| nFDD | 791 | `2 6 12 27 60 132 208 196 114 34` |
| *BMD | 34 | `34` |

Observation：multiplier 的 middle bits 依賴最多 partial products，所以 bitwise DD 會快速變大。*BMD 對 multiplication 明顯比較 compact。

### 5-bit XOR, interleaved order

| DD | Total nodes | Per-output nodes |
|---|---:|---|
| BDD | 10 | `2 2 2 2 2` |
| pFDD | 10 | `2 2 2 2 2` |
| nFDD | 10 | `2 2 2 2 2` |
| *BMD | 15 | `15` |

Observation：Boolean XOR 本來就很適合 BDD/FDD。這個例子也提醒我們：*BMD 不是對所有 function 都最好，它特別適合 word-level arithmetic。

### 4-bit dot2, interleaved order

| DD | Total nodes | Per-output nodes |
|---|---:|---|
| BDD | 81 | `4 21 26 22 8` |
| pFDD | 68 | `4 11 22 23 8` |
| nFDD | 102 | `6 18 37 33 8` |
| *BMD | 14 | `14` |

Observation：pFDD 在這個 dot-product-like function 上比 BDD 小，代表 Davio expansion 對某些 XOR/AND 混合結構可能有幫助。但 *BMD 還是最適合整體 arithmetic expression。

## 圖片範例

- `result/25_LN/figures/add_4_bdd_file_bit4.png`
- `result/25_LN/figures/add_4_bdd_interleaved_bit4.png`
- `result/25_LN/figures/mul_4_bdd_interleaved_bit7.png`
- `result/25_LN/figures/mul_4_pfdd_interleaved_bit7.png`
- `result/25_LN/figures/mul_4_bmd_interleaved.png`

## 結論

1. BDD/FDD 適合 Boolean bit-level function；*BMD 適合 word-level integer arithmetic。
2. 對 addition，interleaved variable order 明顯比 file order 好，因為 related inputs 會被放在一起。
3. 對 multiplication，BDD/FDD 的 node count 在中間 output bits 變大，因為 partial products 最多。
4. pFDD 對一些 XOR-like 或 AND/XOR 混合 function 可能比 BDD 小，但不保證對 multiplier 一定更好。
5. *BMD 對 `add` 和 `mul` 這種 polynomial arithmetic function 很 compact，這符合 lecture note 中希望觀察不同 DD 對 arithmetic circuits 的差異。

## References

- R. E. Bryant, [`Graph-Based Algorithms for Boolean Function Manipulation`](https://www.cs.cmu.edu/~bryant/pubs.html), IEEE TC, 1986.
- R. E. Bryant and Y.-A. Chen, [`Verification of Arithmetic Circuits with Binary Moment Diagrams`](https://www.cs.cmu.edu/~bryant/pubdir/dac95a.pdf), DAC 1995.
