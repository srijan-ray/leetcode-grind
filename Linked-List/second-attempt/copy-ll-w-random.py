from typing import Optional

#"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
#"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_copy_dict = {None : None}

        curr = head
        while curr:
            curr_val = curr.val
            node_copy_dict[curr] = Node(curr_val)
            curr = curr.next

        curr = head
        while curr:
            copied_node = node_copy_dict[curr]
            copied_node.next = node_copy_dict[curr.next]
            copied_node.random = node_copy_dict[curr.random]
            curr = curr.next

        return node_copy_dict[head]
