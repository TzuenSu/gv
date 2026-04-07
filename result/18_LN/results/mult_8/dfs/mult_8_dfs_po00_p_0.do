cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_8.v
breset 2000 8009 30011
bsetorder -dfs
bcons -output 0
brep 480 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/dfs/mult_8_dfs_po00_p_0.bdd.txt
bdraw 480 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/dfs/mult_8_dfs_po00_p_0.dot
q -f
