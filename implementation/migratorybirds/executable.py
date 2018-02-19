#!/usr/bin/python3

import sys

def migratoryBirds(n, ar):
  count = [0] *6
  for i in ar:
    count[int(i)] += 1

  return count.index(max(count))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
