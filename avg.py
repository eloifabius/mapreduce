#!/usr/bin/env python3

import sys, re
regex = re.compile('[^a-zA-Z]')

listparisnum = []


for line in sys.stdin:
    line = line.strip()
    words = line.split(':')
    if len(words) == 3:
        listparisnum.append(words[1])
        print('%s:%s:%s' % (words[0], words[1], words[-1]))
    elif len(words) == 2:
        for num in listparisnum:
            if words[0] == num:
                print('%s:%s' % (words[0], words[-1]))

