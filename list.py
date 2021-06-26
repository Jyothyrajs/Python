#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 22:05:30 2019

@author: jyothyrajs
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l = [[]]
    for i in range(0,n+1):
        for j in range(0,n+1):
            for k in range(0,n+1):
                print(k)
                if((i+j+k)!=n):
                    l.append([i,j,k])
    l.remove([])
    print(l)