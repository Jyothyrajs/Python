#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:20:18 2019

@author: jyothyrajs
"""
from array import array as arr

def findSecLargest(a , n):
    l = a[0]
    sl = a[0]
    if(sl > l):
        l = sl
        sl = a[0]
    
    for i in range(1,n):
        x = a[i]
        if( x > l ):
            sl = l
            l = x
        elif ( x > sl ):
            sl = x
    print('Second Largest: ',sl)
            
def secLargestArray(  ):
    print('No of Elements:')
    n = int(input())
    a = arr('i')
    print('Elements: ')
    for i in range( 0, n ):
        x = int(input())
        a.append(x)
    findSecLargest(a , n)
    
    
def main():
    secLargestArray()

main()