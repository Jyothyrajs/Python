#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
///***Sequences***///
Created on Mon Jun 24 08:58:32 2019

@author: jyothyrajs
"""

Subjects=['Phy','Che',12] #List
Games=['hocky','cricket']
Subjects.append('English')
print(Subjects)
Subjects.append(Games)
print(Subjects)
Subjects.insert(3,'History')
print(Subjects)

Os=('windows','Linux')   #Tuple
#Os.append('Mac') # cannot update

course=[('Phy','Che',12),('windows','Linux')] # List of tuples
print(course[0][2])
print(course[1][0])
for i in course:
    print(course.index(i))


name='Jyothy Sanish' # String
print(name.__len__())
print(name.index('y'))
if 'y' in name:
    print(name.count('y'))
    
    # Set: Collection of unique objects
lang={'C','Java','Python','C'}



#Dictionary
person={'Name':'Jyothy','Age':35}
print(person['Name'])
print(person['Age'])
person['Name']= 'Dhrona'
print(person['Name'])


