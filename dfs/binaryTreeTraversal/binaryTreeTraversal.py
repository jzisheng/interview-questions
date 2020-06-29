'''
Binary Tree Traversals Iterative

'''

from collections import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    pass

class Solution:
    def inorderTraversal(self, root):
        result, stack = [], []
        # stack add left, root, val
        curr = root
        while curr != None or stack:
            while curr != None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result
    
    def postorderTraversal(self, root):
        result, stack = [], []
        # stack add left, right, val
        if not(root): return []        
        stack.append(root)
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.left:
                stack.append(curr.left)            
            if curr.right:
                stack.append(curr.right)
            pass
        
        return result[::-1]

    def preorderTraversal(self,root):        
        result, stack = [], []
        # stack add val, left, right
        stack.append(root)
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return result
        
a = TreeNode(10, \
             left=TreeNode(5,left=TreeNode(1),right=TreeNode(11)), \
             right=TreeNode(15))
s = Solution()
print("")
# 10 1 5 15
# 10 1 5 15
print(s.preorderTraversal(a))

