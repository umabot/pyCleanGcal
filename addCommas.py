# takes an input file and output file
# input file is a Gcal in csv format
# output file: add 2 commas beggining of line if there are no commas in the line

import os, sys

inputFile = open(sys.argv[1], "rt")
outFile = open(sys.argv[2], "wt")

for line in inputFile:
    if line.count(",") == 0:
        strName = line.split("@")[0]
        line = strName + "," + strName + "," + line
    outFile.write(line)

inputFile.close()
outFile.close()
