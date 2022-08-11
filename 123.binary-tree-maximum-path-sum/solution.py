# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.max_thus_far = float('-inf')
        
    def maxPathSumRec(self, node: Optional[TreeNode]) -> int:
        if not node:
            return float('-inf')

        left = self.maxPathSumRec(node.left)
        right = self.maxPathSumRec(node.right)
        
        max_including_node = max(node.val, left + node.val, right + node.val)
        
        self.max_thus_far = max(self.max_thus_far, max_including_node, left, right, left + node.val + right)
        
        return max_including_node

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSumRec(root)
        return self.max_thus_far
