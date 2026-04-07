cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/adder_8.v
breset 2000 8009 30011
bsetorder -rdfs
bcons -output 4
brep 88 -file /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/rdfs/adder_8_rdfs_po04_sum_4.bdd.txt
bdraw 88 /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/rdfs/adder_8_rdfs_po04_sum_4.dot
q -f
