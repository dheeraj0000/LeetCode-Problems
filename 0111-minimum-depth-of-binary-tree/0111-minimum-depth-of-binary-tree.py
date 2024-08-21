# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        elif root.left is None or root.right is None:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))

        else:
            return 1+ min(self.minDepth(root.left), self.minDepth(root.right))