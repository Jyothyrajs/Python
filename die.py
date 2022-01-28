#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 16:18:17 2019

@author: jyothyrajs
"""

from random import randint
import sys
def show_die(n):
    print
    print(n)

def roll_die():
    n = randint(1,6)
    return n

def main():
    try:
        n = roll_die()
        show_die(n)
    except: 
        print("Random number not in range")
main()
