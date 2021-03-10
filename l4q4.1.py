#!/usr/bin/env python3

import sys

dna1 = sys.argv[1]
dna2 = sys.argv[2]
dna3 = sys.argv[3]

strand1 = len(dna1)
strand2 = len(dna2)
strand3 = len(dna3)

if strand1 > strand2 and strand1 > strand3:
    if strand2 > strand3:
        print(dna3 + "," + dna2 + "," + dna1)
    else:
        print(dna2 + "," + dna3 + "," + dna1)

elif strand2 > strand1 and strand2 > strand3:
    if strand1 > strand3:
        print(dna3 + "," + dna1 + "," + dna2)
    else:
        print(dna1 + "," + dna3 + "," + dna2)
else:
    if strand1 > strand2:
        print(dna2 + "," + dna1 + "," + dna3)
    else:
        print(dna1 + "," + dna2 + "," + dna3)
