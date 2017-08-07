#!/usr/bin/python3

import sys

def decibinary(x):
    if x == 1 or x == 2:
      return x - 1
    
    total = 2
    value = 4
    
    while total < x:
      total += value
      value += 4

    value = int((value-4) / 2)
    
    if x >= total-(value/2):
      total -= value*2 
      value += 1

    
  

q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    # your code goes here
    print(decibinary(x))
