'''
0 0 0 0 1 2 3
a b c a a b c
          i
      j

'''

class Solution:
    def repeatedSubstringPattern(self, s):
        n = len(s)
        dp = [0]*n
        for i in range(1,n):
            j = dp[i-1]
            while j > 0 and s[i] != s[j]:
                j = dp[j-1]
            if s[i] == s[j]:
                j += 1
            dp[i] = j
        print(dp)
        sl = dp[n-1]
        return dp[n-1] != 0 and n%(n-sl)==0


s = "babaab"
s = "aabaabaa"
sol = Solution()
print(sol.repeatedSubstringPattern(s))
