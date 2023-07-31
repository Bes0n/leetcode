#!/usr/bin/python3.10

# nums = [7,4,3,9,1,8,5,2,6] 
nums = [5, 2, 7, 10, 3, 9]
target = 8

def getAverages(nums, target):
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in dic: # This operation is O(1)!
            return [nums[i], complement]
        
        dic[num] = i
    
    return [-1, -1]

print(getAverages(nums, target))