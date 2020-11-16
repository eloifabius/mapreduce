#!/usr/bin/env python3

import sys, re
regex = re.compile('[^a-zA-Z]')

city = "Paris"

for line in sys.stdin:
    line = line.strip()
    words = line.split(',')
    if len(words) == 5:
        if words[-1] == city:
            print('%s:%s:%s' % (words[1], words[2], words[-1]))

    elif len(words) == 3:
        print('%s:%s' % (words[0], words[2]))