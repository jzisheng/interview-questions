"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def getEnd(self, node):
        if node.next == None:
            return node
        else:
            return self.getEnd(node.next)

    def connect(self, node):
        a, d = node, node.next
        b, c = node.child, self.getEnd(node.child)
        a.next = b
        a.child = None
        b.prev = a
        c.next = d
        if d:
         d.prev = c
        return a
        
    def flatten(self, head: 'Node') -> 'Node':
        node = head
        while node != None:
            if node.child:
                self.connect(node)
            node = node.next                
        return head

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# a.next = d
d.prev = a
a.child = b
b.next = c
c.prev = b

s = Solution()
res = s.flatten(a)

node = res
while node:
    print(node.val)
    node = node.next
