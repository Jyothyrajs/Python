#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:59:21 2019

@author: jyothyrajs
"""
age=[1,2,3];
section=['A','B'];
section.insert(1,'C');
print(section);
# Append 
age.append(section);
print(age);

del age[1];
print(age);

#Remove first matching object using remove
age[1].pop(1);
print(age);
