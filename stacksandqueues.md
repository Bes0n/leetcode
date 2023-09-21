# Stacks and Queues
## Stacks
A stack is an ordered collection of elements where elements are only added and removed from the same end. In the physical world, an example of a stack would be a stack of plates in a kitchen - you add plates or remove plates from the top of the pile. In the software world, a good example of a stack is the history of your current browser's tab. Let's say you're on site A, and you click on a link to go to site B, then from B you click on another link to go to site C. Every time you click a link, you are adding to the stack - your history is now [A, B, C]. When you click the back arrow, you are "removing" from the stack - click it once and you have [A, B], click it again and you have [A].

Another term used to describe stacks is LIFO, which stands for last in, first out. The last (most recent) element placed inside is the first element to come out.

Stacks are very simple to implement. Some languages like Java have built-in stacks. In Python, you can just use a list `stack = []` and use `stack.append(element)` and `stack.pop()`. In fact, any dynamic array can implement a stack. Typically, inserting into a stack is called `pushing` and removing from a stack is called `popping`. Stacks will usually also come with operations like `peek`, which means looking at the element at the top of the stack.

The time complexity of stack operations is dependent on the implementation. If you use a dynamic array, which is the most common and easiest way, then the time complexity of your operations is the same as that of a dynamic array. O(1) push, pop, and random access, and O(n) search. Sometimes, a stack may be implemented with a linked list with a tail pointer.

```
# Declaration: we will just use a list
stack = []

# Pushing elements:
stack.append(1)
stack.append(2)
stack.append(3)

# Popping elements:
stack.pop() # 3
stack.pop() # 2

# Check if empty
not stack # False

# Check element at top
stack[-1] # 1

# Get size
len(stack) # 1
```

## String problems
String questions involving stacks are popular. Normally, string questions that can utilize a stack will involve iterating over the string and putting characters into the stack, and comparing the top of the stack with the current character at each iteration. Stacks are useful for string matching because it saves a "history" of the previous characters. Let's look at some examples.

**Example 1**: 20. Valid Parentheses

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. The string is valid if all open brackets are closed by the same type of closing bracket in the correct order, and each closing bracket closes exactly one open bracket.

For example, `s = "({})"` and `s = "(){}[]"` are valid, but `s = "(]"` and` s = "({)}"` are not valid.

The order is last in, first out **(LIFO)** - the last opening bracket we saw is the first one we should close, which is perfect functionality for a stack to provide.

```
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {"(": ")", "[": "]", "{": "}"}
        
        for c in s:
            if c in matching: # if c is an opening bracket
                stack.append(c)
            else:
                if not stack:
                    return False
                
                previous_opening = stack.pop()
                if matching[previous_opening] != c:
                    return False
 
        return not stack
```

**Example 2**: 1047. Remove All Adjacent Duplicates In String

You are given a string `s`. Continuously remove duplicates (two of the same character beside each other) until you can't anymore. Return the final string after this.

For example, given `s = "abbaca"`, you can first remove the `"bb"` to get `"aaca"`. Next, you can remove the `"aa"` to get `"ca"`. This is the final answer.

```
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)
```

**Example 3**: 844. Backspace String Compare

Given two strings `s` and `t`, return `true` if they are equal when both are typed into empty text editors. `'#'` means a backspace character.

For example, given `s = "ab#c"` and t = `"ad#c"`, return true. Because of the backspace, the strings are both equal to `"ac"`.

```
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            stack = []
            for c in s:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()

            return "".join(stack)

        return build(s) == build(t)
```

#### Simplify Path
##### My solution
```
class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        stack = []

        for c in s:
            if c != '' and c != '.' and c != '..':
                stack.append(c)
                
            if stack and c == '..':
                stack.pop()
        
        return "/" + "/".join(stack)
        
```

##### Official solution
```
class Solution:
    def simplifyPath(self, path: str) -> str:

        # Initialize a stack
        stack = []

        # Split the input string on "/" as the delimiter
        # and process each portion one by one
        for portion in path.split("/"):

            # If the current component is a "..", then
            # we pop an entry from the stack if it's non-empty
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                # A no-op for a "." or an empty string
                continue
            else:
                # Finally, a legitimate directory name, so we add it
                # to our stack
                stack.append(portion)

        # Stich together all the directory names together
        final_str = "/" + "/".join(stack)
        return final_str
```

#### Simplify Path
##### My solution
```
class Solution:
    def makeGood(self, s: str) -> str:
        string = list(s)
        stack = []

        for curr in string:
            if stack and curr.islower() and stack[-1].isupper():
                if stack[-1].lower() == curr:
                    stack.pop()
                else:
                    stack.append(curr)
            
            elif stack and curr.isupper() and stack[-1].islower():
                if stack[-1].upper() == curr:
                    stack.pop()
                else:
                    stack.append(curr)
            else:
                stack.append(curr)
        
        return "".join(stack)
```

##### Official solution

```
class Solution:
    def makeGood(self, s: str) -> str:
        string = list(s)
        stack = []

        for curr in string:
            if stack and curr == stack[-1].swapcase():
                stack.pop()
            else:
                stack.append(curr)
        
        return "".join(stack)
```

## Queues
While a stack followed a **LIFO** pattern, a queue follows **FIFO** (first in first out). In a stack, elements are added and removed from the same side. In a queue, elements are added and removed from opposite sides. Like with a stack, there are multiple ways to implement a queue, but the important thing that defines it is the abstract interface of adding and removing from opposite sides.

Queues are trickier to implement than stacks if you want to maintain good performance. Like a stack, you could just use a dynamic array, but operations on the front of the array (adding or removal) are `O(n)`, where `n` is the size of the array. Adding to a queue is called enqueue and deletions are called dequeue. If you want these operations to be `O(1)`, you'll need a more sophisticated implementation.

```
# Declaration: we will use deque from the collections module
import collections
queue = collections.deque()

# If you want to initialize it with some initial values:
queue = collections.deque([1, 2, 3])

# Enqueueing/adding elements:
queue.append(4)
queue.append(5)

# Dequeuing/removing elements:
queue.popleft() # 1
queue.popleft() # 2

# Check element at front of queue (next element to be removed)
queue[0] # 3

# Get size
len(queue) # 3
```

**Example: 933**. Number of Recent Calls
Implement the `RecentCounter` class. It should support `ping(int t)`, which records a call at time `t`, and then returns an integer representing the number of calls that have happened in the range `[t - 3000, t]`. Calls to ping will have increasing `t`.

```
from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        
        self.queue.append(t)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
```

#### Moving Average from Data Stream
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

- Implement the `MovingAverage` class:

    - `MovingAverage(int size)` Initializes the object with the size of the window `size`.
    - `double next(int val)` Returns the moving average of the last `size` values of the stream.

##### Official solution
```
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        # number of elements seen so far
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        self.queue.append(val)
        
        if self.count > self.size:
            tail = self.queue.popleft() 
        else: 
            tail = 0

        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.size, self.count)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
```

## Monotonic
A monotonic stack or queue is one whose elements are always sorted. It can be sorted either ascending or descending, depending on the algorithm. Monotonic stacks and queues maintain their sorted property by removing elements that would violate the property before adding new elements. For example, let's say you had a monotonically increasing stack, currently `stack = [1, 5, 8, 15, 23]`. You want to push `14` onto the stack. To maintain the sorted property, we need to first pop the `15` and `23` before pushing the `14` - after the push operation, we have `stack = [1, 5, 8, 14]`.

```
Given an integer array nums

stack = []
for num in nums:
    while stack.length > 0 AND stack.top >= num:
        stack.pop()
    // Between the above and below lines, do some logic depending on the problem
    stack.push(num)
```

As we discussed earlier in the sliding window chapter, despite the nested loop, the time complexity is still *O(n)*, where *n* is the length of the array, because the inner while loop can only iterate over each element once across all for loop iterations, making the for loop iterations amortized *O(1)*.

**Example 1: 739**. Daily Temperatures

Given an array of integers `temperatures` that represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the i-th day to get a warmer temperature. If there is no future day that is warmer, have `answer[i] = 0` instead.

```
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        
        return answer
```

**Example 2: 239**. Sliding Window Maximum

Given an integer array `nums` and an integer `k`, there is a sliding window of size k that moves from the very left to the very right. For each window, find the maximum element in the window.

For example, given `nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`, return `[3, 3, 5, 5, 6, 7]`. The first window is `[1, 3, -1, -3, 5, 3, 6, 7]` and the last window is `[1, 3, -1, -3, 5, 3, 6, 7]`

Note: this problem is significantly more difficult than any problem we have looked at so far. Don't be discouraged if you are having trouble understanding the solution.

```
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()
        for i in range(len(nums)):
            # maintain monotonic decreasing.
            # all elements in the deque smaller than the current one
            # have no chance of being the maximum, so get rid of them
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            # queue[0] is the index of the maximum element.
            # if queue[0] + k == i, then it is outside the window
            if queue[0] + k == i:
                queue.popleft()
            
            # only add to the answer once our window has reached size k
            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans
```