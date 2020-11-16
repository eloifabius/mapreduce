#!/usr/bin/env python3

import sys, re
regex = re.compile('[^a-zA-Z]')

finalist = []
resList = []

for line in sys.stdin:
    line = line.strip()
    words = line.split(':')

    if len(words) == 3:
        finalist.append(words)
        resList.append([words[0], words[1], 0, 0])

    elif len(words) == 2:
        for res in resList:
            if res[1] == words[0]:
                res[2] += int(words[-1])
                res[3] += 1

for r in resList:
    if r[2] != 0 or r[3] != 0:
        try:
            z = r[2]/r[3]
        except ZeroDivisionError:
            z = 0
        
        print('%s:%s' % (r[0], z))

        
