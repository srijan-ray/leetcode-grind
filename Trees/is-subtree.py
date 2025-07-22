# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if self.checkMatching(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        #def findSubRoot(root, subRoot):
        #    foundRoot = root
        #    if root is None:
        #        return None
        #    
        #    if root.val == subRoot.val:
        #        return root
        #    
        #    foundRootLeft = findSubRoot(root.left, subRoot)
        #    foundRootRight = findSubRoot(root.right, subRoot)
        #
        #    if foundRootLeft is not None:
        #        return foundRootLeft
        #    elif foundRootRight is not None:
        #        return foundRootRight
        #    else:
        #        return None
        
        # trueRoot = findSubRoot(root, subRoot)

    def checkMatching(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        
        leftCase = False
        rightCase = False
        if root.val == subRoot.val:
            leftCase = self.checkMatching(root.left, subRoot.left)
            rightCase = self.checkMatching(root.right, subRoot.right)
            

        return leftCase and rightCase
