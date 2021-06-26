#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:47:19 2019

@author: jyothyrajs
"""
import numpy as np
def poly_read():
    coeff=[]
    ip=input()
    x=int(input())
    coeff=ip.split(" ")
    c="."
    for i in range(len(coeff)):
        if(coeff[i].find(c)):
            coeff[i]= float(coeff[i])
        else:
            coeff[i]= int(coeff[i])
   
    print(np.polyval(coeff,x))
    
poly_read()