# Author: Eric Leung
# Date: 2016-05-19
#
# Simple XML parser which parses the value of the <str> tags and 
# write them to the output file, 1 value per line.
#
# Usage: python xmlparser.py [inputFilePath] [outputFilePath]
#
# argv1: Relative or absolute path of the input XML file.
# argv2: Relative or absolute path of the output file.
#

import sys
from xml.dom import minidom

inputFilePath = sys.argv[1]
outputFilePath = sys.argv[2]

xmldoc = minidom.parse(inputFilePath)

## open file for writing
file = open(outputFilePath, 'w');

elements = xmldoc.getElementsByTagName('doc')
print(len(elements))
for e in elements:
		file.write(e.getElementsByTagName('str')[0].firstChild.nodeValue+'\n');
		
## we are done, close file
file.close();