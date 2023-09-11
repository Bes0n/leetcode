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

- Here's some example code for creating a linked list to represent the data `1 --> 2 --> 3`. As you can see, the class that defines a node has a field `val` which will hold the data, and a `next` pointer which references the next node. In the code, we are creating three nodes, one for each number, then setting the `next` pointers accordingly. 