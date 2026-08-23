# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiameter = 0
        
        def height(root):
            nonlocal maxdiameter
            if not root:
                return 0
            leftheight = height(root.left)
            rightheight = height(root.right)

            diameter = leftheight + rightheight
            maxdiameter = max(diameter,maxdiameter)
            return 1 + max(leftheight,rightheight)
        
        height(root)
        return maxdiameter


