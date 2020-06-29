import collections
class Solution:
    def degreeOfArray(self,nums):
        counts = defaultdict(int)        
        for n in nums:
            counts[n] += 1
            pass

    pass

print("")
s = Solution()
s.degreeOfArray([1,2,2,3,1])
