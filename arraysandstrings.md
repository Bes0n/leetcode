# Arrays and Strings
- Why should we care about something being mutable or immutable? If you have a mutable array arr = ["a", "b", "c"] and an immutable string s = "abc", but you want to instead represent "abd", you can easily do arr[2] = "d", but you cannot do s[2] = "d". As such, if you wanted the string s = "abd", you would need to create it entirely from scratch. With such a small string, it's not a big deal. But sometimes you are dealing with strings with 100,000 characters, so creating new versions just to modify one character is very expensive `O(n)`, where `n` is the size of the string.

- As mentioned before, a majority of algorithm problems will involve an array or string. They are extremely versatile data structures and it's impossible to list all the relevant problem-solving techniques in one article. In the next few articles, we'll go over the most common techniques. But first, let's take a quick look at the complexity of array and string operations.

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

##### 557. Reverse Words in a String III
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

```
Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
```

###### My solution

```
# Solution 1 (Faster):
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ans = []
        for word in words:
            ans.append(word[::-1])
        
        return ' '.join(ans)

# Solution 2 (Slower):
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ans = ''

        for w in words:
            word = list(w)
            left, right = 0, len(word) - 1
            while left < right:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
                ans = " ".join(word)
        
        return ans
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

##### Prefix sum
```
# Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13

def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans
```

```
# Example 2: 2270. Number of Ways to Split Array
# Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.

# With Array 
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])

        ans = 0
        for i in range(n - 1):
            left_section = prefix[i]
            right_section = prefix[-1] - prefix[i]
            if left_section >= right_section:
                ans += 1

        return ans

# Without Array
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = left_section = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_section += nums[i]
            right_section = total - left_section
            if left_section >= right_section:
                ans += 1

        return ans
```

###### Running Sum of 1d Array
```
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

#Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
```

###### My Solution
```
class Solution(object):
    def runningSum(self, nums):
        prefix = [nums[0]]
        l = len(nums)
        
        if l <= 1:
            return prefix

        for n in range(1, l):
            prefix.append(prefix[n - 1] + nums[n])

        return prefix
```

###### LeetCode Solution
```
class Solution(object):
    def runningSum(self, nums):
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums
```

##### Minimum Value to Get Positive Step by Step Sum
```
# Given an array of integers nums, you start with an initial positive value startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

# Example 1:
Input: nums = [-3,2,-3,4,2]
Output: 5

Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.

step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2


# Example 2:
Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive. 

# Example 3:
Input: nums = [1,-2,-3]
Output: 5
```

###### My Solution 
```
class Solution(object):
    def minStartValue(self, nums):
        prefix = [nums[0]]
        l = len(nums)
        lowest = nums[0]

        for n in range(1, l):
            presum = prefix[n - 1] + nums[n]
            prefix.append(presum)
            lowest = min(lowest, presum)

        if lowest < 1:
            return (lowest * -1) + 1
        else:
            return 1
```

###### Official Solution 
```
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # We use "total" for current step-by-step total, "min_val" for minimum 
        # step-by-step total among all sums. Since we always start with 
        # startValue = 0, therefore the initial current step-by-step total is 0, 
        # thus we set "total" and "min_val" be 0. 
        min_val = 0
        total = 0

        # Iterate over the array and get the minimum step-by-step total.
        for num in nums:
            total += num
            min_val = min(min_val, total)

        # We have to change the minimum step-by-step total to 1, 
        # by increasing the startValue from 0 to -min_val + 1, 
        # which is just the minimum startValue we want.
        return -min_val + 1
```

##### K Radius Subarray Averages
```
Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]
Explanation:
- avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
- The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.
  Using integer division, avg[3] = 37 / 7 = 5.
- For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
- For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
- avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.
```

###### Official Solution
```
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # When a single element is considered then its averafge will be the number itself only.
        if k == 0:
            return nums

        n = len(nums)
        averages = [-1] * n

        # Any index will not have 'k' elements in it's left and right.
        if 2 * k + 1 > n:
            return averages

        # Generate 'prefix' array for 'nums'.
        # 'prefix[i + 1]' will be sum of all elements of 'nums' from index '0' to 'i'.
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # We iterate only on those indices which have atleast 'k' elements in their left and right.
        # i.e. indices from 'k' to 'n - k'
        for i in range(k, n - k):
            leftBound, rightBound = i - k, i + k
            subArraySum = prefix[rightBound + 1] - prefix[leftBound]
            average = subArraySum // (2 * k + 1)
            averages[i] = average

        return averages
```