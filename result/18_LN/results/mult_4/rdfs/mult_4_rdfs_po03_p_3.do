cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_4.v
breset 2000 8009 30011
bsetorder -rdfs
bcons -output 3
brep 100 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/rdfs/mult_4_rdfs_po03_p_3.bdd.txt
bdraw 100 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/rdfs/mult_4_rdfs_po03_p_3.dot
q -f
