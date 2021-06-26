#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 13:55:19 2019

@author: jyothyrajs
"""
import os
import sys
def timeConversion(s):
    hr,minute,sec =  s.split(':')
    nhr=hr
    if(sec[2:4] == 'PM' and int(hr)<12 ):
        nhr= int(hr)+12
        
    if(sec[2:4] == 'AM' and int(hr)==12):
        nhr = 00
    sec = sec.rstrip(".APM")
    s1 = "{}:{}:{}"
    s2 = "0{}:{}:{}"  
    if(int(nhr)==0):
     return s2.format(nhr,minute,sec)
    return s1.format(nhr,minute,sec)
if __name__ == '__main__':
   # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)

   # f.write(result + '\n')

   # f.close()
