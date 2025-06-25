# pyright: basic
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None

        if head.next is None:
            return None

        slow = head
        fast = head.next

        # Find midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second list
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge
        first, second = head, prev
        while second:
            firstNode = first.next
            secondNode = second.next
            first.next = second
            second.next = firstNode
            first = firstNode
            second = secondNode
