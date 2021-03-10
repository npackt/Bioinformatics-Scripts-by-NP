#!/usr/bin/env python3

import sys

first_name = sys.argv[1]
last_name = sys.argv[2]

first_length = len(first_name)
last_length = len(last_name)

if first_length > last_length:
    print(first_name + " is longer than " + last_name + ".")
elif first_length == last_length:
    print(first_name + " is the same length as " + last_name + ".")
else:
    print(last_name + " is longer than " + first_name + ".")
