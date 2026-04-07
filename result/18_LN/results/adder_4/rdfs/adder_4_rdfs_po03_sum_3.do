cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/adder_4.v
breset 2000 8009 30011
bsetorder -rdfs
bcons -output 3
brep 40 -file /Users/tzuen/Desktop/gv/result/18_LN/results/adder_4/rdfs/adder_4_rdfs_po03_sum_3.bdd.txt
bdraw 40 /Users/tzuen/Desktop/gv/result/18_LN/results/adder_4/rdfs/adder_4_rdfs_po03_sum_3.dot
q -f
