cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/adder_4.v
breset 2000 8009 30011
bsetorder -dfs
bcons -output 4
brep 41 -file /Users/tzuen/Desktop/gv/result/18_LN/results/adder_4/dfs/adder_4_dfs_po04_cout_0.bdd.txt
bdraw 41 /Users/tzuen/Desktop/gv/result/18_LN/results/adder_4/dfs/adder_4_dfs_po04_cout_0.dot
q -f
