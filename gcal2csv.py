# takes an input file and output file
# input file is a Gcal guest list
# output file is each guest per line in the output

import os, sys

inputFile = open(sys.argv[1], "rt")
outFile = open(sys.argv[2], "wt")
data = inputFile.read()

data = data.replace(', ', '\n') # to transpose the gcal input just replace each comma for a new line character

outFile.write(data)

inputFile.close()
outFile.close()