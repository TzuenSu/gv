cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_8.v
breset 2000 8009 30011
bsetorder -dfs
bcons -output 6
brep 486 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/dfs/mult_8_dfs_po06_p_6.bdd.txt
bdraw 486 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/dfs/mult_8_dfs_po06_p_6.dot
q -f
