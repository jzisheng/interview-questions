from sys import path
from os import getcwd

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    pass


class Solution:
    def equals(self, s, t):
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        return s.val == t.val and self.equals(s.left,t.left)\
            and self.equals(s.right, t.right)
        pass
    
    def traverse(self, s, t):
        return self.equals(s,t) or self.traverse(s.left, t) \
            or self.traverse(s.right, t)
        pass
    
    def isSubtree(self, s, t):
        return self.traverse(s,t)
        pass


s = Solution()
a = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
b = TreeNode(4, TreeNode(1), TreeNode(2))
s.isSubtree(a,b)

