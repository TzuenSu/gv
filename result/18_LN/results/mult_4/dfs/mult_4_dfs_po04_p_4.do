cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_4.v
breset 2000 8009 30011
bsetorder -dfs
bcons -output 4
brep 101 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/dfs/mult_4_dfs_po04_p_4.bdd.txt
bdraw 101 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/dfs/mult_4_dfs_po04_p_4.dot
q -f
