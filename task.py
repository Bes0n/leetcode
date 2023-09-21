#!/usr/bin/python3.10

import itertools

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] == 0:
                curr = nums[left]
                nums.append(curr)
                nums.pop(left)
                left += 1
            elif nums[right] == 0:
                curr = nums[right]
                nums.insert(0,curr)
                nums.pop(right)
                right -= 1
            else:
                left, right = left + 1, right - 1

        return nums

# print(Solution.moveZeroes(Solution, nums))

# Declaration: we will use deque from the collections module
import collections
queue = collections.deque()

# If you want to initialize it with some initial values:
queue = collections.deque([1, 2, 3])

# Enqueueing/adding elements:
queue.append(4)
queue.append(5)

# Dequeuing/removing elements:
# queue.popleft() # 1
# queue.popleft() # 2
# print(queue)

# Check element at front of queue (next element to be removed)
# print(queue[0]) # 3
# print(queue[1]) # 3
# print(queue[2]) # 3

# Get size
len(queue) # 3

while queue:
    print(queue)
    print(queue.popleft())