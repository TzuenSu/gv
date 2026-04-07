cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_8.v
breset 2000 8009 30011
bsetorder -dfs
bcons -output 4
brep 484 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/dfs/mult_8_dfs_po04_p_4.bdd.txt
bdraw 484 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/dfs/mult_8_dfs_po04_p_4.dot
q -f
