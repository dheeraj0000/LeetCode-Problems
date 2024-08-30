class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftH = 1
        left = root.left
        while left:
            leftH += 1
            left = left.left

        rightH = 1
        right = root.right
        while right:
            rightH += 1
            right = right.right
        
        if leftH == rightH:
            return pow(2, leftH)-1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)