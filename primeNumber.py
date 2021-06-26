#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 13:41:36 2019

@author: jyothyrajs
"""

def prime(n):
    for i in range(2, int(n/2)):
        if( 0 == n % i ):
            return False
    return True

def generatePrimes(begin, end):
    for i in range(begin, end):
        if(prime(i)):
            print (i, end = ' ')

def main():
    begin = int(input('Number: '))
    end = int(input('Number: '))
    generatePrimes(begin,end)
        
main()
            