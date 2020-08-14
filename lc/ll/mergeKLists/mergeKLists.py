# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
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
        pass
    
    def mergeKLists(self, lists):
        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0, n-interval, interval*2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if n > 0 else None


s = Solution()
a = ListNode(1, ListNode(4, ListNode(6)))
b = ListNode(1, ListNode(3, ListNode(5)))
c = ListNode(4, ListNode(6, ListNode(8)))
res = s.mergeKLists([a,b])

while res:
    print(res.val)
    res = res.next
