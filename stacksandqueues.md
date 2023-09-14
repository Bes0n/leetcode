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

## Middle of the Linked List
### My solution