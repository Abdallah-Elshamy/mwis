#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 10:35:08 2018

@author: Adallah-Elshamy
"""
def mwis(weights , n):
    book_keeper = [0,weights[1]]
    for i in range(2,n+1):
        book_keeper.append(0)
    for i in range(2,n+1):
        book_keeper[i] = max(book_keeper[i-1],book_keeper[i-2]+ weights[i])
    IS = set()
    j = n        
    while(j >= 1):
        if book_keeper[j-1] >= (book_keeper[j-2] + weights[j]):
            j -=1
        else:
            IS.add(j)
            j -= 2
    return IS 



weights = [0]
with open('mwis.txt') as f:
    n = int(f.readline())
    data = f.readlines()
    for line in data:
        weights.append(int(line[:-1]))
       
IS = mwis(weights , n)

ans = ""
for i in [1, 2, 3, 4, 17, 117, 517, 997]:
    if i in IS:
        ans += '1'
    else:
        ans += '0'
print(ans)