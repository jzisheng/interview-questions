'''
7 4 1 4 2

7 7

'''

class Solution:
    def houseRobber(self, nums):
        n = len(nums)
        dp = [0]*(n+1)
        dp[n-1] = nums[n-1]
        dp[n-2] = nums[n-2]        
        for idx in range(n-3,-1,-1):
            dp[idx] = max(nums[idx+1], nums[idx]+dp[idx+2])
        return dp[0]

s = Solution()
print(s.houseRobber([3,4,3,4,3]))
