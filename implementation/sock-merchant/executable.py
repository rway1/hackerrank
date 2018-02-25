#!/bin/python3

import sys

def sockMerchant(n, ar):
    counter_list = [0] * 101
    for item in ar:
        counter_list[item] = counter_list[item] + 1
    
    return sum([int(s/2) for s in counter_list])

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)