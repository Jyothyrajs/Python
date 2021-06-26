#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 12:44:11 2019

@author: jyothyrajs
"""


def findSecLargest(n1, n2, n3):
    if (n1 > n2) :
        if (n2 > n3):
            secLarg = n2 
        elif (n1 > n3):
            secLarg = n3
        else:
            secLarg = n1
    else:
        if( n2 < n3 ):
            secLarg = n2
        elif(n1 < n3):
            secLarg = n3
        else:
            secLarg = n1
    return secLarg
    
def main():
    n1 = int(input("Number 1: "))
    n2 = int(input("Number 2: "))
    n3 = int(input("Number 3: "))
    secLarg = findSecLargest(n1, n2, n3)
    print ( 'Second Largest :', secLarg)
    
main()