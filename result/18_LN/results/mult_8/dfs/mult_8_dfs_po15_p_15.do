cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_8.v
breset 2000 8009 30011
bsetorder -dfs
bcons -output 15
brep 495 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/dfs/mult_8_dfs_po15_p_15.bdd.txt
bdraw 495 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/dfs/mult_8_dfs_po15_p_15.dot
q -f
