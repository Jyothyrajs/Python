#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:34:01 2019

@author: jyothyrajs
"""

# find the number of characters in a file
from array import array as arr

def datainput():
    print("read")
    f=open("die.py",mode='r',encoding='utf-8')
    l=0
    c=10
    f_ch=[]
    print(f_ch)
    print('Appending')
    f_ch.append(f.read().split('='))
    print(f_ch[0],'\n')
   # for line in f:
    #    print(line, end='\n')
     #   l=l+1
   # print('No of lines:',l)
   
def main():
    datainput()
    
main()
     