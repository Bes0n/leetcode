#!/usr/bin/python3.10
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]):
        slow = head
        fast = head
        
        while slow:
            print(slow.val)
            slow = slow.next


print(Solution.deleteDuplicates([1,1,2,3,3]))