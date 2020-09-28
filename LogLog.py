# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:41:05 2020

@author: quasi-researcher
"""

import sys

def lsb_zeroes(num):
  if num == 0:
    return 32 # default for 32 bit integer
  p = 0
  while (num >> p) & 1 == 0:
    p += 1
  return p

k=5 # number (power of two) of buckets to average the estimate
num_buckets = 2 ** k
max_zeroes = [0] * num_buckets
two_r = [0] * num_buckets
with open(r'loglog.txt', 'r') as sf:
    n = sf.readline()
    n = int(n)
    i = 0
    small = True
    s = set()
    for i in range(n):
        req=sf.readline()
        if i < 1000:
            if req not in s:
                s.add(req)
            i+=1
        else:
            small=False
                
        h = hash(req)
        bucket = h & (num_buckets - 1) # create bucket ID
        bucket_hash = h >> k
        max_zeroes[bucket] = max(max_zeroes[bucket], lsb_zeroes(bucket_hash))
        two_r[bucket]=2 ** (-max_zeroes[bucket])
    if small:
        print(len(s))
    else:
        print(int(2 ** (float(sum(max_zeroes)) / num_buckets) * num_buckets * 0.79402))


