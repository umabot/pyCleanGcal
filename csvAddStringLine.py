# takes an input file and output file and a string to add at the end of each line
# input file is a Gcal in csv format
# output file has the string added at the end of each line

import os, sys

inputFile = open(sys.argv[1], "rt")
outFile = open(sys.argv[2], "wt")
str2Add = sys.argv[3]

for line in inputFile:
    outFile.write(line.rstrip('\n') + str2Add + '\n')

inputFile.close()
outFile.close()