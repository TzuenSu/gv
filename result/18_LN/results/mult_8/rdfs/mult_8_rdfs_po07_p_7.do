cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_8.v
breset 2000 8009 30011
bsetorder -rdfs
bcons -output 7
brep 487 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/rdfs/mult_8_rdfs_po07_p_7.bdd.txt
bdraw 487 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/rdfs/mult_8_rdfs_po07_p_7.dot
q -f
