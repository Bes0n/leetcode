# Linked Lists
- Before starting this chapter, you need to have a basic understanding of object-oriented programming concepts, including classes, objects, and attributes.

```
#!/usr/bin/python3.10

class House():
    # House description
    def __init__(self, street, number) -> None:
        self.street = street
        self.number = number
        self.age = 0
    
    def build(self):
        # Building the house
        print("House number {} on street {} has been built".format(self.number, self.street))
    
    def ageofhouse(self, year):
        # Age of House
        self.age += year


House1 = House("Zizkov", 35)
House2 = House("Vinohrady", 10)

# Calling object, Output: Zizkov
print(House1.street)

# Calling object, Output: 10
print(House2.number)

# Calling method, Output: House number 35 on street Zizkov has been built
print(House1.build())

# Calling method and updating age of the house
House1.ageofhouse(5)
print(House1.age) # Output 5
print(House2.age) # Output 0


# Inheritance
class AvenueHouse(House):
    def __init__(self, avenue, number) -> None:
        super().__init__(self, number)
        self.avenue = avenue
        self.number = number

AveHouse = AvenueHouse("Legerova", 25)

# Calling object from super class, Output: Legerova
print(AveHouse.avenue)
```

- Linked list advantages and disadvantages compared to arrays
    - The main advantage of a linked list is that you can add and remove elements at any position in `O(1)`. The caveat is that you need to have a reference to a node at the position in which you want to perform the addition/removal, otherwise the operation is `O(n)`, because you will need to iterate starting from the head until you get to the desired position. However, this is still much better than a normal (dynamic) array, which requires `O(n)` for adding and removing from an arbitrary position.
    - A few other notes that are less relevant for algorithm problems but may come up in an interview discussion - linked lists have the advantage of not having fixed sizes. While dynamic arrays can be resized, under the hood they still are allocated a fixed size - it's just that when this size is exceeded, the array is resized, which is expensive. Linked lists don't suffer from this. However, linked lists have more overhead than arrays - every element needs to have extra storage for the pointers. If you are only storing small items like booleans or characters, then you may be more than doubling the space needed.


- Here's some example code for creating a linked list to represent the data `1 --> 2 --> 3`. As you can see, the class that defines a node has a field `val` which will hold the data, and a `next` pointer which references the next node. In the code, we are creating three nodes, one for each number, then setting the `next` pointers accordingly. 
```
class ListNode():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

one.next = two
two.next = three
head = one

print(head.val) # Output 1
print(head.next.val) # Output 2
print(head.next.next.val) # Output 3
```

- Mechanics of a linked list
    - Understanding how to manipulate linked list nodes and pointers using code is essential not only to solve linked list interview questions, but the underlying concept of handling pointers is fundamental for any software engineer.
    - Assignment `(=)` - When you assign a pointer to an existing linked list node, the pointer refers to the object in memory. Let's say you have a node `head`:

    ```
    ptr = head
    head = head.next
    head = None
    ```
    - After these lines of code, ptr still refers to the original head node, even though the head variable changed. This is the first important concept: variables remain at nodes unless they are modified directly (ptr = something is the only way to modify ptr).

- Chaining `.next`
    - If you have multiple `.next`, for example `head.next.next`, everything before the final .next refers to one node. For example, given a linked list `1 -> 2 -> 3`, if you have head pointing at the first node, and you do `head.next.next`, you are actually referring to `2.next`, because `head.next` is the `2`. We'll soon see that this is a very useful technique.

- Traversal
    - Iterating forward through a linked list can be done with a simple loop. This is the usual code that you will use to do so: as an example let's get the sum of all values from an integer linked list:

    ```
    def get_sum(head):
    ans = 0
    while head:
        ans += head.val
        head = head.next
    
    return ans
    ```

    - The final node's `next` pointer is `null`. Therefore, after doing `head = head.next` at the final node, `head` becomes `null` and the while loop ends.
    - Moving to `head.next` is the equivalent of iterating to the next element in an array. Traversal can also be done recursively:
    
    ```
    def get_sum(head):
    if not head:
        return 0
    
    return head.val + get_sum(head.next)
    ```

## Types of linked lists
### Singly linked list
- This is the most common type of linked list and the one that is given in the code above. In a singly linked list, each node only has a pointer to the next node. This means you can only move forward in the list when iterating. The pointer used to reference the next node is usually called `next`.

- Let's say you want to add an element to a linked list so that it becomes the element at position `i`. To do this, you need to have a pointer to the element currently at position `i - 1`. The next element (currently at position `i`), call it `x`, will be pushed to the element at position `i + 1` after the insertion. This means that `x` should become the `next` node to the one being added, and the node being added should become the next node to the one currently at `i - 1`. Here's some code and images demonstrating:

```
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Let prev_node be the node at position i - 1
def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add
```

- Let's say you want to delete the element at position i. Again, you need to have a pointer to the element currently at position i - 1. The element at position i + 1, call it x, will be shifted over to be at position i after the deletion. Therefore, you should set x as the next node to the element currently at position i - 1. Here's some code and images demonstrating:

```
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Let prev_node be the node at position i - 1
def delete_node(prev_node):
    prev_node.next = prev_node.next.next
```

### Doubly linked list
- A doubly linked list is like a singly linked list, but each node also contains a pointer to the previous node. This pointer is usually called `prev`, and it allows iteration in both directions.

- In a singly linked list, we needed a reference to the node at `i - 1` if we wanted to add or remove at `i`. This is because we needed to perform operations on the `prevNode`. With a doubly linked list, we only need a reference to the node at i. This is because we can simply reference the prev pointer of that node to get the node at `i - 1`, and then do the exact same operations as above.

- With a doubly linked list, we need to do extra work to make also update the prev pointers.

```
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Let node be the node at position i
def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    node.prev = node_to_add

# Let node be the node at position i
def delete_node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node
```

### Linked lists with sentinel nodes
- We call the start of a linked list the `head` and the end of a linked list the `tail`.
- Sentinel nodes sit at the start and end of linked lists and are used to make operations and the code needed to execute those operations cleaner. The idea is that, even when there are no nodes in a linked list, you still keep pointers to a `head` and `tail`. The real `head` of the linked list is `head.next` and the real tail is `tail.prev`. The sentinel nodes themselves are not part of our linked list.
- The previous code we looked at is prone to errors. For example, if we are trying to delete the last node in the list, then `nextNode` will be `null`, and trying to access `nextNode.next` would result in an error. With sentinel nodes, we don't need to worry about this scenario because the last node's `next` points to the sentinel tail.
- The sentinel nodes also allow us to easily add and remove from the front or back of the linked list. Recall that addition and removal is only `O(1)` if we have a reference to the node at the position we are performing the operation on. With the sentinel tail node, we can perform operations at the end of the list in `O(1)`.

```
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def add_to_end(node_to_add):
    node_to_add.next = tail
    node_to_add.prev = tail.prev
    tail.prev.next = node_to_add
    tail.prev = node_to_add

def remove_from_end():
    if head.next == tail:
        return

    node_to_remove = tail.prev
    node_to_remove.prev.next = tail
    tail.prev = node_to_remove.prev

def add_to_start(node_to_add):
    node_to_add.prev = head
    node_to_add.next = head.next
    head.next.prev = node_to_add
    head.next = node_to_add

def remove_from_start():
    if head.next == tail:
        return
    
    node_to_remove = head.next
    node_to_remove.next.prev = head
    head.next = node_to_remove.next

head = ListNode(None)
tail = ListNode(None)
head.next = tail
tail.prev = head
```

### Dummy pointers
As mentioned earlier, we usually want to keep a reference to the `head` to ensure we can always access any element. Sometimes, it's better to traverse using a "dummy" pointer and to keep `head` at the head.

```
def get_sum(head):
    ans = 0
    dummy = head
    while dummy:
        ans += dummy.val
        dummy = dummy.next
    
    # same as before, but we still have a pointer at the head
    return ans
```

# Fast and slow pointers
When the pointers move at different speeds, usually the "fast" pointer moves two nodes per iteration, whereas the "slow" pointer moves one node per iteration (although this is not always the case). Here's some pseudocode:

```
// head is the head node of a linked list
function fn(head):
    slow = head
    fast = head

    while fast and fast.next:
        Do something here
        slow = slow.next
        fast = fast.next.next
```

The reason we need the while condition to also check for `fast.next` is because if `fast` is at the final node, then `fast.next` is null, and trying to access `fast.next.next` would result in an error (you would be doing `null.next`).

- Let's look at some examples where fast and slow pointers can come in handy.

```
# Example 1: Given the head of a linked list with an odd number of nodes head, return the value of the node in the middle.
# For example, given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, return 3.
# As mentioned in the previous article, the easiest way to solve this problem would be to just convert the linked list into an array by iterating over it, and then just returning the number in the middle.

function fn(head):
    array = int[]
    while head:
        array.push(head.val)
        head = head.next

    return array[array.length // 2]

# This is basically "cheating", and would never pass as an acceptable solution in an interview. You may have realized that the difficulty in this problem comes from the fact that we don't know how long the linked list is. One thing we could do is iterate through the linked list once with a dummy pointer to find the length, then iterate from the head again once we know the length to find the middle.

def get_middle(head):
    length = 0
    dummy = head
    while dummy:
        length += 1
        dummy = dummy.next
    
    for _ in range(length // 2):
        head = head.next
    
    return head.val

# The most elegant solution comes from using the fast and slow pointer technique. If we have one pointer moving twice as fast as the other, then by the time it reaches the end, the slow pointer will be halfway through since it is moving at half the speed.

def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val

# The pointers use O(1) space, and if there are `n` nodes in the linked list, the time complexity is O(n) for the traversals.

# Example 2: 141. Linked List Cycle
# Given the head of a linked list, determine if the linked list has a cycle.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

# Why will the pointers always meet, and the fast pointer won't just "skip" over the slow pointer in the cycle? After looping around the cycle for the first time, if the fast pointer is one position behind, then the pointers will meet on the next iteration. If the fast pointer is two positions behind, then it will be one position behind on the next iteration. This pattern continues - after looping around once, the fast pointer moves exactly one step closer to the slow pointer at each iteration, so it's impossible for it to "skip" over.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


- The hashing solution: if you continuously iterate using the next pointer, there are two possibilities:
    - If the linked list doesn't have a cycle, you will eventually reach null and finish.
    - If the linked list has a cycle, you will eventually visit a node twice. We can use a set to detect this.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

# Example 3: Given the head of a linked list and an integer k, return the k^th node from the end.
# For example, given the linked list that represents 1 -> 2 -> 3 -> 4 -> 5 and k = 2, return the node with value 4, as it is the 2nd node from the end.

# If we separate the two pointers by a gap of k, and then move them at the same speed, they will always be k apart. When the fast pointer (the one further ahead) reaches the end, then the slow pointer must be at the desired node, since it is k nodes behind. 

def find_node(head, k):
    slow = head
    fast = head
    for _ in range(k):
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow
```

##### Middle of the Linked List
###### My solution
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
        
```

##### Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
```
Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
```

###### My solution

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head

        while slow and slow.next:
            if slow.val == slow.next.val:
                slow.next = slow.next.next
            else:
                slow = slow.next

        return head
```

# Fast and slow pointers
Imagine that we have a linked list `1 -> 2 -> 3 -> 4`, and we want to return `4 -> 3 -> 2 -> 1`. Let's say we keep a pointer `curr` that represents the current node we are at. Starting with `curr` at the `1`, we need to get the `2` to point to `curr`. The problem is, once we iterate `(curr = curr.next)` to get to the `2`, we no longer have a pointer to the `1` because it is a singly linked list. To get around this, we can use another pointer `prev` that tracks the previous node.

At any given node `curr`, we can set `curr.next = prev` to switch the direction of the arrow. Then, we can update `prev` to be `curr` in preparation for the next node. However, if we change `curr.next`, we will lose that next node. To fix this, we can use a temporary variable `nextNode` to point to the next node before changing any of the other pointers.

```
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next # first, make sure we don't lose the next node
        curr.next = prev      # reverse the direction of the pointer
        prev = curr           # set the current node to prev for the next node
        curr = next_node      # move on
        
    return prev
```

- When we are at a node `curr`, we need to set its `next` pointer to the node we were at previously.
    - Use a `prev` pointer to track the previous node.
- The `prev` pointer needs to also update every iteration.
    - After updating `curr.next`, set `prev = curr` in preparation for the next node.
- If we set `curr.next = prev`, then we lose the reference to the original `curr.next`.
- Use `nextNode` to keep a reference to the original `curr.next`.

##### Example: 24. Swap Nodes in Pairs
- Given the `head` of a linked list, swap every pair of nodes. For example, given a linked list `1 -> 2 -> 3 -> 4 -> 5 -> 6`, return a linked list `2 -> 1 -> 4 -> 3 -> 6 -> 5`.
- Again, let's break down what we need to do step by step, and how we can accomplish it. Consider the first pair of nodes as `A -> B`.

- Starting with `head` at node `A`, we need node `B` to point here.
    - We can accomplish this by doing `head.next.next` = `head`
- However, if we change `B.next`, we will lose access to the rest of the list.
    - Before applying the change in step 1, save a pointer `nextNode = head.next.next`.

- To summarize the steps:
    - Performs an edge swap from `A -> B -> C -> ...` to `A <-> B C -> ...`.
    - Make sure we can still access the rest of the list beyond the current pair (saves `C`).
    - Now that `A <-> B` is isolated from the rest of the list, save a pointer to `A` to connect it with the rest of the list later. Move to the next pair.
    - Connect the previous pair to the rest of the list. In this case connecting `A -> D`.
    - Use a dummy pointer to keep a reference to what we want to return.
    - Handle the case when there's an odd number of nodes.

```
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Check edge case: linked list has 0 or 1 nodes, just return
        if not head or not head.next:
            return head

        dummy = head.next               # Step 5
        prev = None                     # Initialize for step 3
        while head and head.next:
            if prev:
                prev.next = head.next   # Step 4
            prev = head                 # Step 3

            next_node = head.next.next  # Step 2
            head.next.next = head       # Step 1

            head.next = next_node       # Step 6
            head = next_node            # Move to next pair (Step 3)

        return dummy
```