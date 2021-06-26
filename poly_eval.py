#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:47:20 2019

@author: jyothyrajs
"""

import numpy as np
def poly_read():
    coeff=list(map(float,input().split()));
    x= int(input())
    coe=np.array(coeff)
    print(np.polyval(coe,x))
    
    
poly_read()
