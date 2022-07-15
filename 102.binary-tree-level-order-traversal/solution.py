from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rec(self, root: Optional[TreeNode], level, level_list):
        if not root:
            return
        
        if level >= len(level_list):
            level_list.append([root.val])
        else:
            level_list[level].append(root.val)
            
        self.rec(root.left, level+1, level_list)
        self.rec(root.right, level+1, level_list)
            
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        level_order = []
        self.rec(root, 0, level_order)
        
        return level_order
        