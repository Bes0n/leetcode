#!/usr/bin/python3.10

# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

def longestOnes(nums, k):
    left = curr = ans = 0 
    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1
        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans

print(longestOnes(nums,k))