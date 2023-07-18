#!/usr/bin/python3.10


nums = [-7,-3,2,3,11]

left = 0
right = len(nums) - 1

while left < right:
    nums[left] = nums[left] ** 2
    nums[right] = nums[right] ** 2
    left += 1
    right -= 1

if len(nums) % 2 != 0 or len(nums) == 1:
    print(nums[left])
    nums[left] = nums[left] ** 2

sorts = sorted(nums)
print(sorts)
