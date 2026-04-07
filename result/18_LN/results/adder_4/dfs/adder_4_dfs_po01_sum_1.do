cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/adder_4.v
breset 2000 8009 30011
bsetorder -dfs
bcons -output 1
brep 38 -file /Users/tzuen/Desktop/gv/result/18_LN/results/adder_4/dfs/adder_4_dfs_po01_sum_1.bdd.txt
bdraw 38 /Users/tzuen/Desktop/gv/result/18_LN/results/adder_4/dfs/adder_4_dfs_po01_sum_1.dot
q -f
