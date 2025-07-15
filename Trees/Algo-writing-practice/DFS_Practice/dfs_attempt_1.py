import sys
sys.path.append("..")
from tree_def import TreeNode
def explore(node: TreeNode) -> list[int]:
    res = []
    def dfs(node: TreeNode):
        if node is not None:
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

    dfs(node)
    return res
