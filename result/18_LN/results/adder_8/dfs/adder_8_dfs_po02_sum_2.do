cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/adder_8.v
breset 2000 8009 30011
bsetorder -dfs
bcons -output 2
brep 86 -file /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/dfs/adder_8_dfs_po02_sum_2.bdd.txt
bdraw 86 /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/dfs/adder_8_dfs_po02_sum_2.dot
q -f
