# pyright: basic
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return False
        fast, slow = head.next, head

        index = 0
        while fast.next is not None:
            if (fast.val == slow.val):
                return True
            fast = fast.next
            index += 1
            if (index % 2 == 0):
                slow = slow.next

        return False
