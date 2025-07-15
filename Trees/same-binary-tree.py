from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        firstTreeDeque = deque([p])
        secondTreeDeque = deque([q])

        while firstTreeDeque and secondTreeDeque:
            for i in range(len(firstTreeDeque)):
                pNode = firstTreeDeque.pop()
                qNode = secondTreeDeque.pop()

                if pNode is None and qNode is None:
                    continue
                
                if pNode is None or qNode is None or pNode.val != qNode.val:
                    return False
                
                firstTreeDeque.append(pNode.left)
                firstTreeDeque.append(pNode.right)
                secondTreeDeque.append(qNode.left)
                secondTreeDeque.append(qNode.right)
        
        return True
