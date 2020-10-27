'''
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        pass
    pass


def printNodes(head):
    curr = head
    while curr != None:
        print(curr.val)
        curr = curr.next
    pass


def removeNthFromEnd(head,n):
    temp = ListNode(0)
    temp.next = head
    
    ahead = temp
    i = 1
    while(i <= n+1):
        ahead = ahead.next
        i+=1
    
    prev = temp
    while ahead != None:
        ahead = ahead.next
        prev = prev.next
    prev.next = prev.next.next
    return temp.next
        

head = ListNode(1)
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))

nhead = removeNthFromEnd(head,1)
printNodes(nhead)
