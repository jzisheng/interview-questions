import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        '''
        do a level order traversal
        '''
        if not root:
            return []
        stack = collections.deque()
        stack.append((root,0))
        prev = 0
        traversal = [[]]
        while stack:
            cur, level = stack.popleft()
            if level != prev:
                traversal.append([])
            traversal[-1].append(cur.val)
            prev = level
            if cur.left:
                stack.append((cur.left, level+1))
            if cur.right:
                stack.append((cur.right, level+1))
        res = []
        for t in (traversal):
            res.append(t[-1])
        return res


s = Solution()
a = TreeNode(5, TreeNode(3, left=TreeNode(2)),
             TreeNode(10, left=TreeNode(8)))
s.rightSideView(a)
