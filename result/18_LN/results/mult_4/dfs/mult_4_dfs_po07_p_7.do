cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_4.v
breset 2000 8009 30011
bsetorder -dfs
bcons -output 7
brep 104 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/dfs/mult_4_dfs_po07_p_7.bdd.txt
bdraw 104 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/dfs/mult_4_dfs_po07_p_7.dot
q -f
