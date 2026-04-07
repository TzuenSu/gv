cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_8.v
breset 2000 8009 30011
bsetorder -rdfs
bcons -output 2
brep 482 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/rdfs/mult_8_rdfs_po02_p_2.bdd.txt
bdraw 482 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/rdfs/mult_8_rdfs_po02_p_2.dot
q -f
