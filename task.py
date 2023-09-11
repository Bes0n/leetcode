#!/usr/bin/python3.10

class ListNode():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
    
    def get_sum(head):
        ans = 0
        while head:
            ans += head.val
            head = head.next
        
        return ans


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

one.next = two
two.next = three
head = one

print(head.val) # Output 1
print(head.next.val) # Output 2
print(head.next.next.val) # Output 3

print(ListNode.get_sum(head))