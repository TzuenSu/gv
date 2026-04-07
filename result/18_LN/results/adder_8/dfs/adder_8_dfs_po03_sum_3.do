cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/adder_8.v
breset 2000 8009 30011
bsetorder -dfs
bcons -output 3
brep 87 -file /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/dfs/adder_8_dfs_po03_sum_3.bdd.txt
bdraw 87 /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/dfs/adder_8_dfs_po03_sum_3.dot
q -f
