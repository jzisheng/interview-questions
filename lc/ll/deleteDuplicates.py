'''
82. Remove Duplicates from Sorted List II
Medium

2079

113

Add to List

Share
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        pass
    pass


from collections import defaultdict
def deleteDuplicates(head):
    count = defaultdict(int)
    nodes = []
    curr = head

    if not head: return head
    
    while curr != None:
        count[curr.val] += 1
        nodes.append(curr)
        curr = curr.next

    res = []
    for i in range(len(nodes)):
        nval = nodes[i].val
        if count[nval] <= 1:
            res.append(nodes[i])

    for i in range(len(res)):
        nxt = None if i+1 >= len(res) else res[i+1]
        res[i].next = nxt

    return res[0]
    

def printNodes(head):
    curr = head
    while curr != None:
        print(curr.val)
        curr = curr.next
    pass


head = ListNode(3,ListNode(3,ListNode(4,ListNode(4,ListNode(5)))))
head = ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(4,ListNode(4,ListNode(5)))))))


head = deleteDuplicates(head)
printNodes(head)

