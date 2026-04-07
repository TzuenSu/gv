cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_8.v
breset 2000 8009 30011
bsetorder -rdfs
bcons -output 11
brep 491 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/rdfs/mult_8_rdfs_po11_p_11.bdd.txt
bdraw 491 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/rdfs/mult_8_rdfs_po11_p_11.dot
q -f
