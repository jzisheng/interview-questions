class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    pass

class Solution:
    def buildTree(self, inorder, postorder):
        def f(l, r):
            if l > r or not postorder:
                return None
            val = postorder.pop()
            idx = idxMap[val]
            
            node = TreeNode(val)
            
            node.left = f(l, idx-1)
            node.right = f(idx+1, r)
            
            return node
        idxMap = {val:idx for idx, val in enumerate(inorder)}
        return f( 0, len(inorder)-1 )
    
    def traverse(self, node):
        if node == None: return
        self.traverse(node.left)
        print("{}".format(node.val) )
        self.traverse(node.right)       

s = Solution()

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
res = s.buildTree(inorder, postorder)
s.traverse(res)
