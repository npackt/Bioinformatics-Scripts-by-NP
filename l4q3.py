#!/usr/bin/env python3

import sys

seq_1 = sys.argv[1]
seq_2 = sys.argv[2]
seq_3 = sys.argv[3]

gc1 = seq_1.count("G") + seq_1.count("C")
gc2 = seq_2.count("G") + seq_2.count("C")
gc3 = seq_3.count("G") + seq_3.count("C")

if gc1 > gc2 and gc1 > gc3:
    most = seq_1
elif gc2 > gc1 and gc2 > gc3:
    most = seq_2
else:
    most = seq_3


print(most + " has the highest GC content.")