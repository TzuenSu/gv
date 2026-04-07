cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_4.v
breset 2000 8009 30011
bsetorder -rdfs
bcons -output 5
brep 102 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/rdfs/mult_4_rdfs_po05_p_5.bdd.txt
bdraw 102 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/rdfs/mult_4_rdfs_po05_p_5.dot
q -f
