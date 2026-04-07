cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/adder_8.v
breset 2000 8009 30011
bsetorder -rdfs
bcons -output 8
brep 92 -file /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/rdfs/adder_8_rdfs_po08_cout_0.bdd.txt
bdraw 92 /Users/tzuen/Desktop/gv/result/18_LN/results/adder_8/rdfs/adder_8_rdfs_po08_cout_0.dot
q -f
