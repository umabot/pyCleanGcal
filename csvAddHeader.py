# takes an input file and output filem and a header string
# input file is a Gcal in csv format
# output file has the string text as header in first line

import os, sys

inputFile = open(sys.argv[1], "rt")
outFile = open(sys.argv[2], "wt")
strHeader = sys.argv[3] + "\n"

data = inputFile.read()

outFile.write(strHeader)
outFile.write(data)

inputFile.close()
outFile.close()