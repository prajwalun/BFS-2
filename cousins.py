# The isCousins method checks if two nodes (x and y) in a binary tree are cousins.
# Cousins are at the same depth but have different parents.

# Helper Function (find_parent):
#   - Returns the parent of the last node in a path.
#   - If the path has one node, return it; otherwise, return the second-to-last value.

# Helper Function (dfs):
#   - Performs a DFS to find paths to x and y.
#   - Adds the path to self.paths if the current node matches x or y.

# Main Execution:
#   - Initialize self.paths to store paths to x and y.
#   - Call dfs to find both paths.
#   - Check:
#       - Paths to x and y are of the same length (same depth).
#       - Parents of x and y are different.

# TC: O(n) - Each node is visited once.
# SC: O(h + k) - Space for recursion stack and paths.


from typing import Optional


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def find_parent(l: list)-> int:
            if len(l) == 1:
                return l[0]
            else:
                return l[-2]
        self.paths = []
        def dfs(root, x, y, path):
            if not root:
                return
            path = path + [root.val]
            if root.val == x or root.val == y:
                self.paths.append(path)
            dfs(root.left,x,y,path)
            dfs(root.right,x,y,path)
        dfs(root,x,y, path = [])
        
        return (len(self.paths[0]) == len(self.paths[1])) and (find_parent(self.paths[0]) != find_parent(self.paths[1]))