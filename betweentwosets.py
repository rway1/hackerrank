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
  y = []
  for i in range(1,x+1):
    if x%i == 0:
      y.append(i)
  return y

def getTotalX(a, b):
  g = Gcd(b)
  l = Lcm(a)
  z = findFactors(g)
  total = 0
  for i in z:
    if i % l == 0:
      total += 1

  return total

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
