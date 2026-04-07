cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/adder_8.v
breset 2000 8009 30011
bsetorder -dfs
bcons -output 6
brep 90 -file /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/dfs/adder_8_dfs_po06_sum_6.bdd.txt
bdraw 90 /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/dfs/adder_8_dfs_po06_sum_6.dot
q -f
