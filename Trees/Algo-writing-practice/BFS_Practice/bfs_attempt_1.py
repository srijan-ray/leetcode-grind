from collections import deque
import sys
sys.path.append("..")
from tree_def import TreeNode
def explore(node: TreeNode) -> list[int]:
    res = []
    queue = deque([node])
    def bfs(node: TreeNode):
        while queue:
            for _ in range(len(queue)):
                currNode = queue.popleft()
                if currNode is None:
                    continue
                res.append(currNode.val)
                queue.append(currNode.left)
                queue.append(currNode.right)

    bfs(node)
    return res

