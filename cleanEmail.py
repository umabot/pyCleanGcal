# takes an input file and output file
# input file is a Gcal in csv format
# output file the emails assumed ecnlosed in <email@domain.com> are converted to email@domain.com

import os, sys

inputFile = open(sys.argv[1], "rt")
outFile = open(sys.argv[2], "wt")

data = inputFile.read()

data = data.replace('<','')
data = data.replace('>','')

outFile.write(data)

inputFile.close()
outFile.close()