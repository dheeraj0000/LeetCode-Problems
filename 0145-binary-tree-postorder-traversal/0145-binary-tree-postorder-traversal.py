# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #postorder-> left-right-root
        def postOrder(root,res):
            if root is None:
                return
            else:
                postOrder(root.left,res)
                postOrder(root.right,res)
                res.append(root.val)
            
            return res
        
        return postOrder(root,[])