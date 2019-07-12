# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 23:00:19 2019

@author: Anushka N Sharma
"""

#find the duplicate number on a given integer array

s=input()
nslist=s.split(',')
nlist=list()
for x in nslist:
    nlist.append(int(x))
d=dict()
for x in nlist:
    if x in d:
        d[x]+=1
    else:
        d[x]=1
print(d)