cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_4.v
breset 2000 8009 30011
bsetorder -rdfs
bcons -output 6
brep 103 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/rdfs/mult_4_rdfs_po06_p_6.bdd.txt
bdraw 103 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/rdfs/mult_4_rdfs_po06_p_6.dot
q -f
