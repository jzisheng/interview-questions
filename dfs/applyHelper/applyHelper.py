'''
Tree Job Application Applier
You have a list of recruiters you need to contact. Each recruiter has
 one and only one parent node. All directly linked recruiters keep tabs
 on each other and will discard your application if you apply to both of them.
 Each recruiter has an associated number of positions.

Determine maximum number positions you can get your application sent to,
 without having application discarded

    [3]
    / \
   2   3
    \   \
    [3] [1]
max: 7

      3
     / \
   [4]  [5]
   / \   \
  1  3    1

max: 9


     3
    / \
    2  [5]
  /  \   \
 [1] [4]  1
max: 10

Solution:
For each node, store the maximum of sums for the children, or neighboring
nodes. 

For example consider the left subtree of node.

Return tuples (a,c), where a cannot be added to node.val as it is neighboring, so it
is the sum of children. This can be added to d or b, as they are not directly connected.

Vice versa for opposite.

     node
    /    \
   a      b
  /\      /\
 /c \    /d \

'''

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def applyHelper(root):
    def f(node):
        if node == None:
            return (0,0)
        a,b = f(node.left)
        c,d = f(node.right)
        neiMax = max(node.val+b+d,b+c,a+d)
        childMax = max(b+d,a+c)
        return ((neiMax,childMax))
    return max(f(root))

a1 = TreeNode(3)
b2 = TreeNode(3)
b1 = TreeNode(2)
c1 = TreeNode(3)
c2 = TreeNode(1)

a1.left = b1
a1.right = b2
b1.right = c1
b2.right = c2

print(applyHelper(a1))
