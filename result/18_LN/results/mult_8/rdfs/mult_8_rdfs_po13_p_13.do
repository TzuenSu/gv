cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_8.v
breset 2000 8009 30011
bsetorder -rdfs
bcons -output 13
brep 493 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/rdfs/mult_8_rdfs_po13_p_13.bdd.txt
bdraw 493 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/rdfs/mult_8_rdfs_po13_p_13.dot
q -f
