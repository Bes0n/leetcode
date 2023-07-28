#!/usr/bin/python3.10

nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13

def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        # print(prefix[-1])
        # print(nums[i])
        prefix.append(nums[i] + prefix[-1])
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        print(curr)
        ans.append(curr < limit)

    # return ans

# [1, 7, 10, 12, 19, 21]
# x = 1 10 10
# y = 12 21 19 

print(answer_queries(nums, queries, limit))