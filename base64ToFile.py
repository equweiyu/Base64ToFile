#!/usr/bin/env python
import base64
import sys
inputFile = sys.argv[1]
outputFile = sys.argv[2]
with open(inputFile, 'r') as input, open(outputFile, 'wb') as output:
    output.write(base64.b64decode(input.read()))
