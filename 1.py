# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 22:21:33 2019

@author: Anushka N Sharma
"""

#find missing number in given integer array 1-100

s=input()
nslist=s.split(',')
nlist=list()
for x in nslist:
    nlist.append(int(x))
nlist.sort()
count=1
i=0
c=0
while count<=10:
    if i<len(nlist):
        if nlist[i]!=count:
            print(count)
            count+=1
        else:
            i+=1
            count+=1
    else:
        if c<1:
            for x in range(count,11):
                print(x)
                c=1
        
