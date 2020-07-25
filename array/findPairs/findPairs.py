'''
3 1 4 1 5
1 1 3 4 5
        ^
5-2 in array?
[5,3]

res = set(
(1,3)
(3,5)
)


'''


class Solution:
    def findPairs(self, nums, k):
        s = set()
        res = set()
        for idx, n in enumerate(nums):
            if n-k in s:
                res.add((n-k,n))
            s.add(n)
            pass
        print(res)
        return len(res)


s = Solution()
nums = [3, 1, 4, 1, 5]
k= 2
print(s.findPairs(nums,k))

