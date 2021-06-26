#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:30:24 2019

@author: jyothyrajs
"""

import numpy as n
import sys

sd=[1,2,3]
td=[(1,2,3),(4,5,6)]
print(sd)
print (td)
print (sys.getsizeof(6)*len(sd))
print (sys.getsizeof(6)*len(td))

L1=range(100)
L2=range(100)

A1= n.arange(100)
A2= n.arange(100)
