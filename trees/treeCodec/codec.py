import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = []
        q.append(root)
        res = ''
        # do a level order traversal
        while q:
            node = q.pop(0)
            if node == None:
                res += 'None,'
                continue
            else:
                res += '{},'.format(node.val)
                q.append(node.left)
                q.append(node.right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(',')
        root = TreeNode(nodes[0])
        q = [root]
        i = 1
        while q and i < len(nodes):
            node = q.pop(0)
            if nodes[i] != 'None':
                node.left = TreeNode(nodes[i])
                q.append(node.left)
            i+=1
            if nodes[i] != 'None':
                node.right = TreeNode(nodes[i])
                q.append(node.right)
            i += 1
        return root
            


c = Codec()
a = TreeNode(5, TreeNode(3, left=TreeNode(2)),
             TreeNode(10, left=TreeNode(8)))
a = TreeNode(-1, TreeNode(0), TreeNode(1))
data = (c.serialize(a))
print(data)
print(c.serialize(c.deserialize(data)))

