# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left,root.right = root.right,root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
# total time is O(n).
# Space: O(h)
# The space comes from the recursion call stack, where h is the tree height.
# Balanced tree: O(log n)
# Completely skewed tree: O(n) worst case