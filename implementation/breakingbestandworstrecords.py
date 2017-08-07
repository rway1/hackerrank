#!/usr/bin/python3

import sys


#returns [number of highest record breaks, number of lowest record breaks]
def getRecord(s):
  ma = s[0]
  mi = ma
  macount = 0
  micount = 0
  for i in s:
    if i > ma:
      ma = i
      macount += 1
    if i < mi:
      mi = i
      micount += 1
  return [macount, micount]

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
