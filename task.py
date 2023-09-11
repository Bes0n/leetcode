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
    
    def add_node(prev_node, node_to_add):
        node_to_add.next = prev_node.next
        prev_node.next = node_to_add
    
    def get_output(head):
        while head:
            return head


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)

one.next = two
two.next = three
head = one

print(head.val) # Output 1
print(head.next.val) # Output 2
print(head.next.next.val) # Output 3
ListNode.add_node(two, four)
print(ListNode.get_output(one)) # Output 6