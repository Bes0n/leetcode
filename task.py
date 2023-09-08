#!/usr/bin/python3.10
from collections import defaultdict

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
matches = [[2,3],[1,3],[5,4],[6,4]]
matches = [[1,7],[1,16],[1,17],[3,10],[4,5],[4,11],[4,16],[5,6],[5,9],[5,12],[5,17],[5,19],[6,15],[7,8],[7,9],[7,12],[8,11],[8,14],[8,18],[8,19],[9,11],[10,11],[10,19],[11,18],[12,16],[12,17],[15,18],[16,19]]

def findWinners(matches):
    l = defaultdict(int)
    losers = []
    winners = []
    for m in matches:
        l[m[1]] += 1

    for n in matches:
        if n[0] not in l.keys():
            print(n)

    # for n in matches:
    #     l[n[1]] += 1
    
    # for key, value in l.items():
    #     if value == 0:
    #         winners.append(key)
    #     elif value == 1:
    #         losers.append(key)
    
    # return sorted(winners), sorted(losers)

print(findWinners(matches))