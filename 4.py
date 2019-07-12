# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 23:12:20 2019

@author: Anushka N Sharma
"""

#find all pairs of an integer array whose sum is equal to a given number
s=input()
target=int(input())
nslist=s.split(',')
nlist=list()
for x in nslist:
    nlist.append(int(x))
#subarr=[]
nlist.sort()
if len(nlist)%2==0:
    n=len(nlist)
else:
    n=len(nlist)+1
for i in range(int(n/2)):
    for j in range(i+1,len(nlist)):
        sum=nlist[i]+nlist[j]
        if sum==target:
            print('(',nlist[i],',',nlist[j],')')
            print('(',nlist[j],',',nlist[i],')')
        
        