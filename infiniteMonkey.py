#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:41:45 2019

@author: jyothyrajs
"""
import random
def generateStr(strlen):
    alphabet="abdgro"
    gstr=""
    for i in range(strlen):
        gstr=gstr+alphabet[random.randrange(6)]
    return gstr

def score(gstr,goal):
    runScore=0
    for i in range(len(gstr)):
        if(gstr[i]==goal[i]):
            runScore=runScore+1
        return runScore/len(goal)
def main():
    m_str="dog"
    newStr=generateStr(3)
    while(score(newStr,m_str)<1):
       newStr= generateStr(3)
       print(newStr)
        
main()