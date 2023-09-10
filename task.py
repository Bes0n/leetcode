#!/usr/bin/python3.10
import collections

jewels = "aA"
stones = "aAAbbbb"

def numJewelsInStones(jewels, stones):
    j = collections.Counter(jewels)
    s = collections.Counter(stones)

    print(j)
    print(s)
    

print(numJewelsInStones(jewels, stones))