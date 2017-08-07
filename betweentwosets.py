#!/usr/bin/python3

#algorithm

#1) L = LCM(a)
#2) G = GCD(b)
#3) F = factors(G)
#4) solution = count of x in F, where x % l is 0

import sys

#calculates gcd of two integers
def gcd(x, y):

   while(y):
       x, y = y, x % y

   return x

#calculates lcm of two integers 
def lcm(x, y):

   lcm = (x*y)//gcd(x,y)
   return lcm

#calculates gcd of list
def Gcd(x):
  g = x[0]
  for i in x:
    g = gcd(g,i)
  return g

#calculates lcm of list
def Lcm(x):
  l = x[0]
  for i in x:
    l = lcm(l,i)
  return l

#returns list of factors for integer
def findFactors(x):
  return [ i for i in range(1,x+1) if x%i == 0]

#calculates number of x, where x % a[i] == 0 for 0 <= i <= n
# and b[i] % x == 0 for 0 <= i <= n
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
