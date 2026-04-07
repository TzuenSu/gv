cirread -v /Users/tzuen/Desktop/gv/result/18_LN/designs/mult_8.v
breset 2000 8009 30011
bsetorder -file
bcons -output 5
brep 485 -file /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/file/mult_8_file_po05_p_5.bdd.txt
bdraw 485 /Users/tzuen/Desktop/gv/result/18_LN/results/mult_8/file/mult_8_file_po05_p_5.dot
q -f
