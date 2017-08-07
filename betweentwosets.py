#!/usr/bin/python3

import sys

def gcd(x, y):

   while(y):
       x, y = y, x % y

   return x

def lcm(x, y):

   lcm = (x*y)//gcd(x,y)
   return lcm

def Gcd(x):
  g = x[0]
  for i in x:
    g = gcd(g,i)
  return g

def Lcm(x):
  l = x[0]
  for i in x:
    l = lcm(l,i)
  return l

def findFactors(x):
  return [ i for i in range(1,x+1) if x%i == 0]

def getTotalX(a, b):
  g = Gcd(b)
  l = Lcm(a)
  return sum( 1 if i % l == 0 else 0 for i in findFactors(g))

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
