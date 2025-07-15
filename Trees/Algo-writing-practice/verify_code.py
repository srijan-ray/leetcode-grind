import sys
import os
from collections import deque

# Import the TreeNode class from tree_def.py
try:
    from tree_def import TreeNode # type: ignore
    print("Successfully imported TreeNode from tree_def.py")
except ImportError:
    print("Error: Could not import TreeNode from tree_def.py.")
    print("Please ensure 'tree_def.py' exists in the same directory as this script and defines 'TreeNode'.")
    # Fallback definition if import fails, though fixing tree_def.py is recommended
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
        def __repr__(self):
            return f"TreeNode({self.val})"


# --- Import User's DFS Code ---
# Assuming your dfs_attempt_1.py is in a folder named DFS-Practice
current_dir = os.path.dirname(__file__)
dfs_path = os.path.join(current_dir, 'DFS-Practice')
if dfs_path not in sys.path:
    sys.path.append(dfs_path)

try:
    from DFS_Practice import dfs_attempt_1
    print("Successfully imported dfs_attempt_1.py")
    # Assuming the DFS function is named 'dfs' within the module
    user_dfs_function = dfs_attempt_1.explore
except ImportError as e:
    print(e)
    print(f"Error: Could not import dfs_attempt_1.py from {dfs_path}.")
    print("Please ensure 'DFS-Practice' folder exists and 'dfs_attempt_1.py' is inside it.")
    user_dfs_function = None
except AttributeError:
    print("Error: 'dfs' function not found in dfs_attempt_1.py.")
    print("Please ensure your DFS function is named 'dfs'.")
    user_dfs_function = None

# --- Import User's BFS Code ---
# Assuming your bfs_attempt_1.py is in a folder named BFS-Practice
bfs_path = os.path.join(current_dir, 'BFS-Practice')
if bfs_path not in sys.path:
    sys.path.append(bfs_path)

try:
    from BFS_Practice import bfs_attempt_1
    print("Successfully imported bfs_attempt_1.py")
    # Assuming the BFS function is named 'bfs' within the module
    user_bfs_function = bfs_attempt_1.explore
except ImportError:
    print(f"Error: Could not import bfs_attempt_1.py from {bfs_path}.")
    print("Please ensure 'BFS-Practice' folder exists and 'bfs_attempt_1.py' is inside it.")
    user_bfs_function = None
except AttributeError:
    print("Error: 'bfs' function not found in bfs_attempt_1.py.")
    print("Please ensure your BFS function is named 'bfs'.")
    user_bfs_function = None


def build_sample_tree():
    """
    Builds a sample binary tree for testing.
          1
         / \
        2   3
       / \   \
      4   5   6
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root

def get_expected_dfs_preorder(root):
    """Helper to get expected DFS (preorder) traversal for verification."""
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def get_expected_bfs(root):
    """Helper to get expected BFS traversal for verification."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def main():
    print("\n--- Starting Tree Traversal Tests ---")

    # Build the sample tree
    tree_root = build_sample_tree()
    print("Sample Tree Structure:")
    # Simple representation for visualization
    # Level 0: 1
    # Level 1: 2, 3
    # Level 2: 4, 5, None, 6

    # Test DFS
    if user_dfs_function:
        print("\n--- Testing DFS ---")
        try:
            dfs_result = user_dfs_function(tree_root)
            print(f"Your DFS result: {dfs_result}")
            expected_dfs = get_expected_dfs_preorder(tree_root)
            print(f"Expected DFS result (Preorder): {expected_dfs}")

            if dfs_result == expected_dfs:
                print("DFS Test: PASSED!")
            else:
                print("DFS Test: FAILED! Results do not match expected (Preorder).")
                print("Note: DFS can have different valid traversals (preorder, inorder, postorder).")
                print("This test expects a preorder traversal. Please adjust your DFS or the test if needed.")
        except Exception as e:
            print(f"An error occurred during DFS execution: {e}")
    else:
        print("\nDFS test skipped due to import/function error.")

    # Test BFS
    if user_bfs_function:
        print("\n--- Testing BFS ---")
        try:
            bfs_result = user_bfs_function(tree_root)
            print(f"Your BFS result: {bfs_result}")
            expected_bfs = get_expected_bfs(tree_root)
            print(f"Expected BFS result: {expected_bfs}")

            if bfs_result == expected_bfs:
                print("BFS Test: PASSED!")
            else:
                print("BFS Test: FAILED! Results do not match expected.")
        except Exception as e:
            print(f"An error occurred during BFS execution: {e}")
    else:
        print("\nBFS test skipped due to import/function error.")

    print("\n--- Tree Traversal Tests Complete ---")

if __name__ == "__main__":
    main()
