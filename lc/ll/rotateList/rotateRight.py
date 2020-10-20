class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def rotateRight(head,k):

    def getSize(node):
        res = 0
        while node:
            res += 1
            node = node.next
        return res
    
    def getEnd(node):
        while node.next:
            node = node.next
        return node
    
    def getNthNode(node,nth):
        for _ in range(nth):
            node = node.next
        return node

    if k == 0 or head is None:
        return head
    
    tail = getEnd(head)
    numNodes = getSize(head)
    k = k%numNodes

    if numNodes == 1 or k % numNodes == 0:
        return head

    end = getNthNode(head,k)
    newTail = head
    
    while end.next:
        end = end.next
        newTail = newTail.next

    newHead = newTail.next
    end.next = head
    
    newTail.next = None
    
    return newHead

def printNodes(head):
    while head != None:
        print(head.val)
        head = head.next

val = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
printNodes(val)
print("==")
res = rotateRight(val,2)
print("==")
printNodes(res)

