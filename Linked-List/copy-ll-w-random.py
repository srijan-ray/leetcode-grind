from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None): # type: ignore

        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyDict: dict[Optional[Node], Optional[Node]] = {None : None}

        curr = head
        while curr:
            copy = Node(curr.val)
            copyDict[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = copyDict[curr] # type: ignore
            copyDict[curr].next = copyDict[curr.next] # type: ignore
            copyDict[curr].random = copyDict[curr.random] # type: ignore
            curr = curr.next
        
        return copyDict[head]
