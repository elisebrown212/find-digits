#Created by: Elise Brown
#!/bin/python

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    count = 0
    n = int(raw_input().strip())
    splitter = str(n)
    for digit in splitter:
        if int(digit) == 0:
            continue
        if n%int(digit) == 0:
            count+=1
    print count