'''
memoized:

LIS(i,k)

base:
i == n: return 0
general:
if nums[i] > k
  return max( 1+LIS(i+1,nums[i]) , LIS(i+1,k) )
else:
  return LIS(i+1,k)

            i      j
[10,9,2,5,3,7,101,18]
              ^   ^
  0 0 0 0 0 2  1  1

LIS(i):
base:
LIS(n-1) = 1

general:
LIS(i) = max(LIS(i), 1+LIS(j)  if nums[j] > nums[i] where j > i



'''

class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [0]*(n)
        dp[n-1] = 1

        for i in range(n-2,-1,-1):
            dp[i] = 1
            for j in range(i+1,n):
                if nums[i] < nums[j]:
                    dp[i] = max(1+dp[j],dp[i])
        return max(dp)


nums = [10,9,2,5,3,7,101,18]
s = Solution()
print(s.lengthOfLIS(nums))
