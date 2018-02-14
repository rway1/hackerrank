#!/usr/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
  count = 0
  for idx,ival in enumerate(ar[0:n-1]):
    for _,jval in enumerate(ar[idx+1:]):
      if (ival+jval)%k == 0:
        count += 1
  return count

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
