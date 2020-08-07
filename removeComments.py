try:
    in_name = input("enter the name of a python file: ")
    inf = open(in_name,"r")
except:
    print ("a problem was encountered while opening the input file")
    print ("quitting")
    quit()

try:
    out_name = input("enter the name of the output file: ")
    outf = open(out_name,"w")
except:
    print ("a problem was encountered while opening the input file")
    print ("quitting")
    quit()

try:
    for line in inf:
        pos = line.find("#")
        if pos > -1:
            line = line[0 : pos]
            line = line + "\n"

        outf.write(line)

    inf.close()
    outf.close()
    print("your file has been saved")

except:
    print ("a problem was found while opening the input file")
    print ("quitting")
