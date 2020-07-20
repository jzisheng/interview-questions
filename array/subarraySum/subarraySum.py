class Solution:
    def subarraySum(self, nums, k):
        cums = set()
        cumsum = 0
        res = 0
        for n in nums:
            cumsum+=n
            cums.add(cumsum)
            if cumsum == k or cumsum-k in cums:
                res += 1
        return res
        pass


s = Solution()
nums = [1,1,1]
s.subarraySum(nums,2)
