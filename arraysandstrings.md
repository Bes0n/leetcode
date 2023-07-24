# Arrays and Strings
##### Two Pointers
###### Check if word is a Palindrome
```
def check_if_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True
```

###### Pair of numbers that sum to target
```
def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1
    
    return False
``` 

###### Sort two arrays by using two pointers
```
def combine(arr1, arr2):
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    
    return ans
```

###### Is Subsequence
```
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
```

##### Reverse string
```
# Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

# Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

###### My solution
```
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            x = s[right]
            y = s[left]
            s[right] = y
            s[left] = x
            left += 1
            right -= 1
        return s
```

###### Official solution
```
class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)
```

##### Squares of a Sorted Array
```
# Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

# 
Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

###### My solution
```
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            nums[left] = nums[left] ** 2
            nums[right] = nums[right] ** 2
            left += 1
            right -= 1

        if len(nums) % 2 != 0 or len(nums) == 1:
            nums[left] = nums[left] ** 2

        sorts = sorted(nums)
        return(sorts)
```

###### Official solution
```
# Approach 1: Sort
class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)

# Approach 2: Two Pointer
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result
```

##### Sliding window
###### Length of the longest subarray
```
nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8

def find_length(nums, k):
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans
```

###### Longest substring achievable that contains only "1"
```
s = "1101100111"

def find_length(s):
    left = curr = ans = 0 
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans
```

###### Subarray Product Less Than K.
```
nums = [10, 5, 2, 6]
k = 100

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = left = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1

        return ans
```

###### Sum of the subarray with the largest sum whose length is k
```
nums = [3, -1, 4, 12, -8, 5, 6]
k = 4

def find_best_subarray(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]
    
    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    
    return ans
```


###### Maximum Average Subarray I
```
# Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:
Input: nums = [5], k = 1
Output: 5.00000
```

###### My solution
```
class Solution(object):
    def findMaxAverage(self, nums, k):
        ans = cur = 0
        if len(nums) == 1:
            return nums[0]

        for i in range(k):
            cur += nums[i]

        ans = cur

        for i in range(k, len(nums)):
            cur +=  nums[i] - nums[i - k]
            
            if cur > ans:
                ans = float(max(ans, cur))

        ans = float(max(ans, cur))
        
        return ans / k
```

###### Max Consecutive Ones III
```
# Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

###### Official Solution
```
    def longestOnes(self, nums, k):
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
```
