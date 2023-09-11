# Hashing
Hash tables can also take up more space. Dynamic arrays are actually fixed-size arrays that resize themselves when they go beyond their capacity. Hash tables are also implemented using a fixed size array - remember that the size is a limit set by the programmer. The problem is, resizing a hash table is much more expensive because every existing key needs to be re-hashed, and also a hash table may use an array that is significantly larger than the number of elements stored, resulting in a huge waste of space. Let's say you chose your limit as 10,000 items, but you only end up storing 10. Okay, you could argue that 10,000 is too large, but then what if your next test case ends up needing to store 100,000 elements? The point is, when you don't know how many elements you need to store, arrays are more flexible with resizing and not wasting space.

##### Interface guide
```
# Declaration: a hash map is declared like any other variable. The syntax is {}
hash_map = {}

# If you want to initialize it with some key value pairs, use the following syntax:
hash_map = {1: 2, 5: 3, 7: 2}

# Checking if a key exists: simply use the `in` keyword
1 in hash_map # True
9 in hash_map # False

# Accessing a value given a key: use square brackets, similar to an array.
hash_map[5] # 3

# Adding or updating a key: use square brackets, similar to an array.
# If the key already exists, the value will be updated
hash_map[5] = 6

# If the key doesn't exist yet, the key value pair will be inserted
hash_map[9] = 15

# Deleting a key: use the del keyword. Key must exist or you will get an error.
del hash_map[9]

# Get size
len(hash_map) # 3

# Get keys: use .keys(). You can iterate over this using a for loop.
keys = hash_map.keys()
for key in keys:
    print(key)

# Get values: use .values(). You can iterate over this using a for loop.
values = hash_map.values()
for val in values:
    print(val)

# Get keys and values
items = my_hash_map.items()

for key, val in items:
    print(f"{key}: {val}")
```

##### Checking for existence
```
# Example 1: 1. Two Sum
# Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. You cannot use the same index twice.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic: # This operation is O(1)!
                return [i, dic[complement]]
            
            dic[num] = i
        
        return [-1, -1]

# Example 2: 2351. First Letter to Appear Twice
# Given a string s, return the first character to appear twice. It is guaranteed that the input will have a duplicate character.

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)

        return " "

# Example 3: Given an integer array nums, find all the numbers x that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.

def find_numbers(nums):
    ans = []
    nums = set(nums)

    for num in nums:
        if (num + 1 not in nums) and (num - 1 not in nums):
            ans.append(num)
    
    return ans
```

##### Check if the Sentence Is Pangram
```
# Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

# Example 2:

Input: sentence = "leetcode"
Output: false
```

###### My Solution 
```
class Solution(object):
    def checkIfPangram(self, sentence):
        seen = set()
        for n in sentence:
            if n not in seen:
                seen.add(n)

            if len(seen) == 26:
                return True

        return False
```

###### Official Solution
```
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Add every letter of 'sentence' to hash set 'seen'.
        seen = set(sentence)
        
        # If the size of 'seen' is 26, then 'sentence' is a pangram.
        return len(seen) == 26
```

##### Missing Number
```
# Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
```

###### My Solution
```
class Solution(object):
    def missingNumber(self, nums):
        nset = set(nums)
        l = len(nums)
        for n in range(l):
            if n not in nset:
                return n

        return l
```

###### Official Solution
```
class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
```

##### Counting Elements
```
# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

# Example 1:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

# Example 2:
Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.
```

###### My Solution
```
class Solution(object):
    def countElements(self, arr):
        n = set(arr)
        total = 0
        for x in arr:
            if x + 1 in n:
                total += 1
        return total
```

###### Official Solution
```
def countElements(self, arr: List[int]) -> int:
    hash_set = set(arr)
    count = 0
    for x in arr:
        if x + 1 in hash_set:
            count += 1
    return count
```

##### Checking for existence
```
# Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".

from collections import defaultdict

def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans

# Example 2: Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.
# For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.

from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for arr in nums:
            for x in arr:
                counts[x] += 1

        n = len(nums)
        ans = []
        for key in counts:
            if counts[key] == n:
                ans.append(key)
        
        return sorted(ans)

# Example 3: 1941. Check if All Characters Have Equal Number of Occurrences
# Given a string s, determine if all characters have the same frequency.
# For example, given s = "abacbc", return true. All characters appear twice. Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.

from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        frequencies = counts.values()
        return len(set(frequencies)) == 1

# Example 4: 560. Subarray Sum Equals K
# Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1
    
        return ans

# Example 5: 1248. Count Number of Nice Subarrays
# Given an array of positive integers nums and an integer k. Find the number of subarrays with exactly k odd numbers in them.
# For example, given nums = [1, 1, 2, 1, 1], k = 3, the answer is 2. The subarrays with 3 odd numbers in them are [1, 1, 2, 1, 1] and [1, 1, 2, 1, 1].

from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0
        
        for num in nums:
            curr += num % 2
            ans += counts[curr - k]
            counts[curr] += 1

        return ans
```

##### Find Players With Zero or One Losses
###### My solution
```
class Solution(object):
    def findWinners(self, matches):
        l = defaultdict(int)
        losers, winners = [], []

        for m in matches:
            l[m[0]] = 0

        for n in matches:
            l[n[1]] += 1

        for key, value in l.items():
            if value == 0:
                winners.append(key)
            elif value == 1:
                losers.append(key)

        return sorted(winners), sorted(losers)
```

###### Official solution
```
# Example 1: Hash Map + Hash Set
class Solution: 
    def findWinners(self, matches : List[List[int]]) ->List[List[int]]: 
        seen = set() losses_count = {}
        
        for winner, loser in matches:
            seen.add(winner)
            seen.add(loser)
            losses_count[loser] = losses_count.get(loser, 0) + 1
        
        #Add players with 0 or 1 loss to the corresponding list.
        zero_lose, one_lose = [], []
        for player in seen:
            count = losses_count.get(player, 0)
            if count == 0:
                zero_lose.append(player)
            elif count == 1:
                one_lose.append(player)
        
        return [sorted(zero_lose), sorted(one_lose)]

# Example 2: Hash Map
class Solution: 
    def findWinners(self, matches: List[List[int]]) ->List[List[int]]: 
        losses_count = {}
        
        for winner, loser in matches:
            losses_count[winner] = losses_count.get(winner, 0)
            losses_count[loser] = losses_count.get(loser, 0) + 1
        
        zero_lose, one_lose = [], []
        for player, count in losses_count.items():
            if count == 0:
                zero_lose.append(player)
            if count == 1:
                one_lose.append(player)
        
        return [sorted(zero_lose), sorted(one_lose)]
```

##### Largest Unique Number
###### My solution
```
    h = defaultdict(int)
    ans = -1

    for n in nums:
        h[n] += 1
    
    for k, v in h.items():
        if v == 1:
            ans = max(ans, k)
    return ans
```

##### Largest Unique Number
###### My solution
```
def maxNumberOfBalloons(text):
    b = {
        'b': 1,
        'a': 1,
        'l': 2,
        'o': 2,
        'n': 1
    }
    h = defaultdict(int)
    if len(text) < 7:
        return 0
    
    for c in text:
        if c in b:
            h[c] += 1
    
    for c in h:
        h[c] = h[c] // b[c]

    return min(h.values())
```

##### More hashing examples
```
# Example 1: 49. Group Anagrams
# Given an array of strings strs, group the anagrams together.
# For example, given strs = ["eat","tea","tan","ate","nat","bat"], return [["bat"],["nat","tan"],["ate","eat","tea"]].

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        
        return groups.values()


# Example 2: 2260. Minimum Consecutive Cards to Pick Up
# Given an integer array cards, find the length of the shortest subarray that contains at least one duplicate. If the array has no duplicates, return -1.

from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = defaultdict(list)
        for i in range(len(cards)):
            dic[cards[i]].append(i)
            
        ans = float("inf")
        for key in dic:
            arr = dic[key]
            for i in range(len(arr) - 1):
                ans = min(ans, arr[i + 1] - arr[i] + 1)
        
        return ans if ans < float("inf") else -1

# Example 3: 2342. Max Sum of a Pair With Equal Sum of Digits
# Given an array of integers nums, find the maximum value of nums[i] + nums[j], where nums[i] and nums[j] have the same digit sum (the sum of their individual digits). Return -1 if there is no pair of numbers with the same digit sum.

from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            
            return digit_sum
        
        dic = defaultdict(list)
        for num in nums:
            digit_sum = get_digit_sum(num)
            dic[digit_sum].append(num)
        
        ans = -1
        for key in dic:
            curr = dic[key]
            if len(curr) > 1:
                curr.sort(reverse=True)
                ans = max(ans, curr[0] + curr[1])
        
        return ans

# Example 4: 2352. Equal Row and Column Pairs
# Given an n x n matrix grid, return the number of pairs (R, C) where R is a row and C is a column, and R and C are equal if we consider them as 1D arrays.

from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def convert_to_key(arr):
            # Python is quite a nice language for coding interviews!
            return tuple(arr)
        
        dic = defaultdict(int)
        for row in grid:
            dic[convert_to_key(row)] += 1
        
        dic2 = defaultdict(int)
        for col in range(len(grid[0])):
            current_col = []
            for row in range(len(grid)):
                current_col.append(grid[row][col])
            
            dic2[convert_to_key(current_col)] += 1

        ans = 0
        for arr in dic:
            ans += dic[arr] * dic2[arr]
        
        return ans
```

##### Ransom Note
###### My solution
```
from collections import defaultdict

ransomNote = "aab"
magazine = "aabb"

def canConstruct(ransomNote, magazine):
    mag = defaultdict(int)
    note = defaultdict(int)

    l = len(ransomNote)
    m = len(magazine)

    if l > m:
        return False
    
    for c in ransomNote:
        note[c] += 1

    for c in magazine:
        if c in note:
            mag[c] += 1
    
    for c in note:
        if note[c] > mag[c]:
            return False
        
    return True
```

###### Official solution
```
def canConstruct(self, ransomNote: str, magazine: str) -> bool:

    # Check for obvious fail case.
    if len(ransomNote) > len(magazine): return False

    # In Python, we can use the Counter class. It does all the work that the
    # makeCountsMap(...) function in our pseudocode did!
    magazine_counts = collections.Counter(magazine)
    ransom_note_counts = collections.Counter(ransomNote)
    
    # For each *unique* character in the ransom note:
    for char, count in ransom_note_counts.items():
        # Check that the count of char in the magazine is equal
        # or higher than the count in the ransom note.
        magazine_count = magazine_counts[char]
        if magazine_count < count:
            return False
            
    # If we got this far, we can successfully build the note.
    return True
```

##### Jewels and Stones
- You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

- Letters are case sensitive, so "a" is considered a different type of stone from "A".

```
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

###### My solution

```
# Solution 1:
from collections import defaultdict

jewels = "aA"
stones = "aAAbbbb"

def numJewelsInStones(jewels, stones):
    jewel = set(jewels)
    stone = defaultdict(int)
    total = 0

    for s in stones:
        if s in jewel:
            stone[s] += 1

    for j in jewel:
        if j in stone:
            total += stone[j]
    
    return total

# Solution 2:
import collections

jewels = "aA"
stones = "aAAbbbb"

def numJewelsInStones(jewels, stones):
    jewel = set(jewels)
    stone = collections.Counter(stones)
    total = 0
    
    for j in jewel:
        if j in stone:
            total += stone[j]
    
    return total
```

###### Official solution

```
class Solution(object):
    def numJewelsInStones(self, J, S):
        Jset = set(J)
        return sum(s in Jset for s in S)
```

##### Longest Substring Without Repeating Characters
- Given a string s, find the length of the longest substring without repeating characters.

```
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

###### Official solution

```
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res
```