#!/usr/bin/python3

import sys

def solve(n, s, d, m):
  return sum( 1 for idx,_ in enumerate(s[:n-(m-1)]) if sum(s[idx:idx+m]) == d)

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
