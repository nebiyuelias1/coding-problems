from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalancedRec(self, node: Optional[TreeNode]):
        if not node:
            return [True, 0]
        
        left_subtree = self.isBalancedRec(node.left)
        right_subtree = self.isBalancedRec(node.right)
        
        if not left_subtree[0]:
            return [False, 0]
        
        if not right_subtree[0]:
            return [False, 0]
        
        height_diff = abs(left_subtree[1] - right_subtree[1])
        if height_diff > 1:
            return [False, 0]
        
        return [True, 1 + max(left_subtree[1], right_subtree[1])]
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedRec(root)[0]