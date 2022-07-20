from typing import Optional

from numpy import absolute


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rec(self, root: Optional[TreeNode], absolute_min: Optional[int], absolute_max: Optional[int]) -> bool:
        if not root:
            return True
        
        if absolute_min and root.val <= absolute_min:
            return False
        if absolute_max and root.val >= absolute_max:
            return False
        
        if root.left and root.val <= root.left.val:
            return False
        if root.right and root.val >= root.right.val:
            return False
        
        min_left = None
        max_left = root.val
        min_right = root.val
        max_right = None
        if absolute_min:
            if absolute_min < root.val:
                min_left = absolute_min
        if absolute_max:
            if absolute_max > root.val:
                max_right = absolute_max
            
        left = self.rec(root.left, absolute_min=min_left, absolute_max=max_left)
        right = self.rec(root.right, absolute_min=min_right, absolute_max=max_right)
        
        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.rec(root, None, None)

three = TreeNode(val=3)
seven = TreeNode(val=7)
six = TreeNode(val=6, left=three, right=seven)
four = TreeNode(val=4)
five = TreeNode(val=5, left=four, right=six)

sol = Solution()
sol.isValidBST(five)