# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 23:07:58 2019

@author: Anushka N Sharma
"""
#find the largest and smallest number in an unsorted integer array

s=input()
nslist=s.split(',')
nlist=list()
for x in nslist:
    nlist.append(int(x))
print('largest: ',max(nlist))
print('smallest: ',min(nlist))
