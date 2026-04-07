cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_8.v
breset 2000 8009 30011
bsetorder -rdfs
bcons -output 10
brep 490 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/rdfs/mult_8_rdfs_po10_p_10.bdd.txt
bdraw 490 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/rdfs/mult_8_rdfs_po10_p_10.dot
q -f
