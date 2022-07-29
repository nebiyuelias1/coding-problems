# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestorRec(self, node: TreeNode, p: TreeNode, q: TreeNode) -> List:
        if not node:
            return [False, None]
        
        l = self.lowestCommonAncestorRec(node.left, p, q)
        r = self.lowestCommonAncestorRec(node.right, p, q)
        
        if l[0] and r[0]:
            return [True, node]
        
        if (node.val == p.val or node.val == q.val) and (l[0] or r[0]):
            return [True, node]
        
        new_node = l[1] if l[1] else r[1]
        
        if node.val == p.val or node.val == q.val:
            return [True, new_node]
        
        return [l[0] or r[0], new_node]
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lowestCommonAncestorRec(root, p, q)[1]