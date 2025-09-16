#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        columns = line.strip().split(",")
        weather = columns[-1].strip().lower()
        print(f"{weather}\t1")
    except:
        continue
