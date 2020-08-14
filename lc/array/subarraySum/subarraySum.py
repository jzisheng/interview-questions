

from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k):
        count, sums = 0,0
        d = defaultdict(int)
        d[0] = 1
        for n in nums:
            sums += n
            if (sums-k) in d:
                count += d[(sums-k)]
            d[sums] += 1
        return count

s = Solution()
print(s.subarraySum([1,1,1],2))
            
