#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 19:56:20 2019

@author: jyothyrajs
"""

if __name__ == '__main__':
    grade = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grade.append([name,score])
    min_grade = grade[0][1]
    sec_min = grade[1][1]
    for i in range(len(grade)-1):
        if( grade[i][1] > sec_min):
            min_grade =sec_min
            sec_min = grade[i][1]
        else: 
            if(grade[i][1] < min_grade):
                min_grade = grade[i][1]
    for i in range(len(grade)):
        if(grade[i][1] == sec_min):
            print(grade[i][0])
        
