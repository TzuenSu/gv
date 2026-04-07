cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/adder_4.v
breset 2000 8009 30011
bsetorder -rdfs
bcons -output 1
brep 38 -file /Users/tzuen/Desktop/gv/result/18_LN/results/adder_4/rdfs/adder_4_rdfs_po01_sum_1.bdd.txt
bdraw 38 /Users/tzuen/Desktop/gv/result/18_LN/results/adder_4/rdfs/adder_4_rdfs_po01_sum_1.dot
q -f
