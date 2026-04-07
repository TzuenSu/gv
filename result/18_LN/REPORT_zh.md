# BDD Variable Ordering 實驗報告

## 目標

本實驗使用 GV 對加法器與乘法器建立 BDD，並比較不同變數排序對 BDD 大小的影響。除了原本的 `BSETOrder -File` 和 `BSETOrder -RFile`，我也在 GV 中新增：

- `BSETOrder -DFS`
- `BSETOrder -RDFS`

`-DFS` 的做法是從所有 PO 和 FF input 出發，使用 circuit 已有的 post-order DFS list，依序收集 PI/current-state variables 作為 BDD variable order。`-RDFS` 則使用相反順序。

## 檔案位置

- Verilog designs: `result/18_LN/designs/`
- 自動化實驗腳本: `result/18_LN/scripts/run_bdd_experiments.py`
- 完整實驗結果: `result/18_LN/results/`
- 完整 CSV 表格: `result/18_LN/results/summary.csv`
- 完整 Markdown 表格與圖片連結: `result/18_LN/README.md`

## 實驗設計

Designs:

- `adder_4.v`
- `mult_4.v`
- `adder_8.v`
- `mult_8.v`

Variable orders:

- `file`: Verilog input declaration order, which is effectively `a[0], a[1], ..., b[0], b[1], ...`
- `dfs`: structural DFS order from PO cones, which tends to collect related bits such as `a[0], b[0], a[1], b[1], ...` for ripple adders
- `rdfs`: reverse structural DFS order

每個 PO 都獨立跑一個 GV process，並設定 timeout，避免 multiplier 某個 PO 若 BDD 爆炸會卡住整批實驗。

## 結果摘要

| Design | Order | BDD sizes by PO | Total | Max |
|---|---|---:|---:|---:|
| `adder_4` | file | 3, 6, 13, 28, 42 | 92 | 42 |
| `adder_4` | dfs | 3, 5, 8, 11, 12 | 39 | 12 |
| `adder_4` | rdfs | 3, 5, 8, 11, 12 | 39 | 12 |
| `mult_4` | file | 3, 7, 17, 41, 47, 46, 37, 25 | 223 | 47 |
| `mult_4` | dfs | 3, 7, 19, 63, 50, 37, 28, 15 | 222 | 63 |
| `mult_4` | rdfs | 3, 7, 13, 30, 48, 55, 40, 16 | 212 | 55 |
| `adder_8` | file | 3, 6, 13, 28, 59, 122, 249, 504, 758 | 1742 | 758 |
| `adder_8` | dfs | 3, 5, 8, 11, 14, 17, 20, 23, 24 | 125 | 24 |
| `adder_8` | rdfs | 3, 5, 8, 11, 14, 17, 20, 23, 24 | 125 | 24 |
| `mult_8` | file | 3, 7, 17, 41, 101, 257, 635, 1645, 2915, 2870, 2492, 2027, 1554, 1026, 675, 453 | 16718 | 2915 |
| `mult_8` | dfs | 3, 7, 19, 63, 183, 511, 1523, 4647, 3976, 3077, 2193, 1458, 1058, 655, 338, 135 | 19846 | 4647 |
| `mult_8` | rdfs | 3, 7, 13, 30, 62, 144, 325, 777, 1775, 3537, 4419, 3872, 2362, 1165, 520, 167 | 19178 | 4419 |

## 圖片範例

- `adder_8` file order cout: `result/18_LN/results/adder_8/file/adder_8_file_po08_cout_0.png`
- `adder_8` dfs order cout: `result/18_LN/results/adder_8/dfs/adder_8_dfs_po08_cout_0.png`
- `mult_8` file order peak PO: `result/18_LN/results/mult_8/file/mult_8_file_po08_p_8.png`
- `mult_8` dfs order peak PO: `result/18_LN/results/mult_8/dfs/mult_8_dfs_po07_p_7.png`
- `mult_8` rdfs order peak PO: `result/18_LN/results/mult_8/rdfs/mult_8_rdfs_po10_p_10.png`

## 討論

對 ripple-carry adder 來說，`file` order 會把所有 `a` bits 放在所有 `b` bits 前面，因此 carry chain 在 BDD 中需要跨過很多不相關的變數。這會造成 BDD 大小快速成長。在 `adder_8` 中，file order 的最大 BDD size 是 758，而 DFS/RDFS 只有 24。

DFS order 對 adder 特別好，因為從每個 sum/cout 的 fanin cone 做 post-order DFS 時，會自然把同一個 bit position 的 `a[i]` 和 `b[i]` 放近。這符合加法器 bit-wise aligned 的結構，因此 carry 可以被比較局部地表示。

對 multiplier 來說，情況比較複雜。低位元 product 只依賴少量 partial products，中間位元依賴最多 cross terms，所以 BDD size 通常在中間輸出附近達到高峰。這次 `mult_8` 中，file order 的 maximum 是 2915，DFS 是 4647，RDFS 是 4419；也就是 DFS heuristic 不一定會優於 file order。

## 結論與 Heuristics

1. 對加法器，好的 variable order 應該依 bit position 交錯排列，例如 `a[0], b[0], a[1], b[1], ...`，因為 addition 是 bit-wise aligned。
2. 對乘法器，單純 DFS 不一定最好，因為 partial product 有大量交錯依賴；中間 output bits 的 BDD 通常最大。
3. 一個實用 heuristic 是把同一個 local logic cone 中會直接互動的 input variables 放近。
4. DFS/RDFS 是便宜且自動化的 structural heuristic，適合當 baseline；但對 arithmetic circuits，最好再搭配 domain knowledge，例如 adder 用 bit-interleaving，multiplier 可嘗試依 partial-product diagonal 或 output cone 分群。
5. 實驗上應該同時測 forward/reverse order，因為 reverse order 有時會讓部分高位或低位輸出變小。
