# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftheight = self.maxDepth(root.left)
        rightheight = self.maxDepth(root.right)

        return 1 + max(leftheight,rightheight)

# Time: O(n)
# Every node is visited exactly once. 
# At each node, you do constant work (compare two numbers, add 1).
# Total work = O(n) where n = number of nodes.

# Space: O(h)
# where h = height of the tree. This is the call stack — each recursive call
# stays "open" (waiting) until its children finish, so the maximum stack
# depth equals how deep the tree goes.
# Balanced tree: O(log n)
# Completely skewed tree (basically a linked list): O(n)