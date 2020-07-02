class Solution:
    def minDistance(self,word1,word2):
        def dp(word1,word2,i,j):
            if i >= len(word1) or j >= len(word2):
                return 0
            if word1[i] == word2[j]:
                return dp(word1,word2,i+1,j+1)
            else:
                replace = 1+dp(word1,word2,i+1,j+1)
                insert = 1+dp(word1,word2,i,j+1)
                delete = 1+dp(word1,word2,i+1,j)
                return min(replace,insert,delete)
        return dp(word1,word2,0,0)


s = Solution()
print(s.minDistance("abc","dec"))
