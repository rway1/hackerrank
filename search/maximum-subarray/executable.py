#!/bin/python3

import sys

def maximumSum(a, m):
    # Complete this function

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        a = list(map(int, input().strip().split(' ')))
        result = maximumSum(a, m)
        print(result)