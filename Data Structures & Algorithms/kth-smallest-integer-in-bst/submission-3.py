# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res =[]
        def invert(root):
            if not root:
                return 
            invert(root.left)
            res.append(root.val)
            invert(root.right)
        invert(root)
        return res[k-1]
#Time: O(n), Space: O(n)