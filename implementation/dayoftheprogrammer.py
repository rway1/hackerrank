#!/usr/bin/python3

import sys


def solve(year):
  result = ".09."+str(year)
  if year < 1918 and year % 4 == 0:
    return "12"+result
  if year > 1919 and (year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)):
    return "12"+result
  if year == 1918:
    return "26.09.1918"
  return "13.09."+str(year)

year = int(input().strip())
result = solve(year)
print(result)
