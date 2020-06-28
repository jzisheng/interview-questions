'''
94. Binary Tree Inorder Traversal
Medium

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
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
    
    def postOrder(self, root):
        result, stack = [], []
        # stack add val, left, right
        stack.append(root)
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)                
        return result

    def preOrder(self,root):
        result, stack = [], []
        # stack add val, left, right
        stack.append(root)
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)                
        return result
        
            
'''
a = TreeNode(10,left=TreeNode(5),right=TreeNode(15))
s = Solution()
print("")
print(s.postOrder(a))
'''
