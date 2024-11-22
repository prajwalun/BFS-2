# The rightSideView method returns the values of the nodes visible from the right side of a binary tree.

# Helper Function (dfs):
#   - Performs a depth-first search to traverse the tree.
#   - Parameters:
#       - 'node': The current node being processed.
#       - 'depth': The current depth of traversal.
#   - Base Case:
#       - If the current node is None, return.
#   - If the current depth equals the length of 'res', append the current node's value to 'res'.
#       - This ensures the first node encountered at each depth (rightmost) is added.
#   - Recursively call dfs for the right and left children, prioritizing the right subtree.

# Main Execution:
#   - Initialize 'res' as an empty list to store the right-side view.
#   - Call dfs starting from the root at depth 0.
#   - Return 'res', which contains the right-side view of the tree.

# TC: O(n) - Each node is visited once.
# SC: O(h) - Space for recursion stack proportional to the tree height.



from typing import Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res