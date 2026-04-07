cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_4.v
breset 2000 8009 30011
bsetorder -dfs
bcons -output 1
brep 98 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/dfs/mult_4_dfs_po01_p_1.bdd.txt
bdraw 98 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/dfs/mult_4_dfs_po01_p_1.dot
q -f
