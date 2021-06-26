#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:28:12 2019

@author: jyothyrajs
"""

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    l=len(a)
    
    for i in range(l,0):
        print(i)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()