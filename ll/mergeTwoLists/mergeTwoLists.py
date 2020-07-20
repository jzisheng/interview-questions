class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    pass


class Solution():
    def mergeTwoLists(self, l1, l2):
        a, b = l1, l2
        while a and b:
            if a.val > b.val:
                temp = b.next
                b.next = a
                b = temp
            else:
                temp = a.next
                a.next = b
                a = temp
        
        if l1.val < l2.val:
            return l1
        return l2
        pass



a = ListNode(1, ListNode(4, ListNode(6)))
b = ListNode(1, ListNode(3, ListNode(5)))
s = Solution()

res = s.mergeTwoLists(a,b)
while res:
    print(res.val)
    res = res.next
    
