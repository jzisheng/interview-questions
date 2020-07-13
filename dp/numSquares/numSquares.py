import math

class Solution:
    def numSquares(self, n):
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(1, n+1):
            nSqrt = int(math.sqrt(i))+1
            for j in range(1, nSqrt):
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[n]

   
s = Solution()
s.numSquares(3)
