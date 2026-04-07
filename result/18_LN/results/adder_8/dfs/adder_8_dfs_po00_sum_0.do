cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/adder_8.v
breset 2000 8009 30011
bsetorder -dfs
bcons -output 0
brep 84 -file /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/dfs/adder_8_dfs_po00_sum_0.bdd.txt
bdraw 84 /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/dfs/adder_8_dfs_po00_sum_0.dot
q -f
