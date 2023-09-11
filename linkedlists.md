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