# takes an input file and output file
# input file is a Gcal in csv format
# output file split the inpiut in commas by replacing spaces by commas

import os, sys

inputFile = open(sys.argv[1], "rt")
outFile = open(sys.argv[2], "wt")
data = inputFile.read()

data = data.replace(' ', ',')

outFile.write(data)

inputFile.close()
outFile.close()