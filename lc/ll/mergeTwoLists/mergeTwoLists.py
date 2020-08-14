class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    pass


class Solution():
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


a = ListNode(1, ListNode(4, ListNode(6)))
b = ListNode(1, ListNode(3, ListNode(5)))
s = Solution()

res = s.mergeTwoLists(a,b)
while res:
    print(res.val)
    res = res.next
    
