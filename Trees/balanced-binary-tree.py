# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(currNode):
            if not currNode:
                return [True, 0]
            
            left, right = dfs(currNode.left), dfs(currNode.right)
            currHeight = abs(left[1] - right[1])
            currBalanced = right[0] and left[0]
            return [currBalanced and currHeight <= 1, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]
