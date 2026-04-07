cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_4.v
breset 2000 8009 30011
bsetorder -rdfs
bcons -output 2
brep 99 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/rdfs/mult_4_rdfs_po02_p_2.bdd.txt
bdraw 99 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_4/rdfs/mult_4_rdfs_po02_p_2.dot
q -f
