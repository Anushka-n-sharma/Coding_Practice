# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 23:56:50 2019

@author: Anushka N Sharma
"""

#duplicates removed from a given array
s=input()
nslist=s.split(',')
nlist=list()
for x in nslist:
    nlist.append(int(x))
nset=set(nlist)
for x in nset:
    print(x,end=' ')
