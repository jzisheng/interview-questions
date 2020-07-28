class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    pass

class Solution:
    def buildTree(self, inorder, postorder):
        def f(inL, inR):
            if inL > inR:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            idx = idxMap[val]
            root.right = f(idx+1, inR)
            root.left = f(inL, idx-1)
            return root
            pass
        idxMap = {val:idx for idx,val in enumerate(inorder)}
        return f(0, len(postorder)-1)

s = Solution()

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
node = s.buildTree(inorder, postorder)
