#!/bin/python3

import sys

def sockMerchant(n, ar):
    counter_list = [0] * 101
    for item in ar:
        counter_list[item] = counter_list[item] + 1
    
    pair_count = 0

    for item in counter_list:
        pair_count = pair_count + int(item/2)
    
    return pair_count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)