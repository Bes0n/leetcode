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