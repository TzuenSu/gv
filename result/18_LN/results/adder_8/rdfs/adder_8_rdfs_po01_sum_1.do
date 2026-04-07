cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/adder_8.v
breset 2000 8009 30011
bsetorder -rdfs
bcons -output 1
brep 85 -file /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/rdfs/adder_8_rdfs_po01_sum_1.bdd.txt
bdraw 85 /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/rdfs/adder_8_rdfs_po01_sum_1.dot
q -f
