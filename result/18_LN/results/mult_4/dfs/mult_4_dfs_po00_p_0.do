cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_4.v
breset 2000 8009 30011
bsetorder -dfs
bcons -output 0
brep 97 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/dfs/mult_4_dfs_po00_p_0.bdd.txt
bdraw 97 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/dfs/mult_4_dfs_po00_p_0.dot
q -f
