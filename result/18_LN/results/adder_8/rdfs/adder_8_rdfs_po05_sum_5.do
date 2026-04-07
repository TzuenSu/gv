cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/adder_8.v
breset 2000 8009 30011
bsetorder -rdfs
bcons -output 5
brep 89 -file /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/rdfs/adder_8_rdfs_po05_sum_5.bdd.txt
bdraw 89 /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/rdfs/adder_8_rdfs_po05_sum_5.dot
q -f
