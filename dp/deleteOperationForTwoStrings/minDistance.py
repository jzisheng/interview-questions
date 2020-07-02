'''
583. Delete Operation for Two Strings
Medium

Share
Given two words word1 and word2, find the minimum number
 of steps required to make word1 and word2 the same,
 where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" 
and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.

'''

class Solution:
    def minDistance(self, word1, word2):
        self.memo = {}
        m,n = len(word1),len(word2)
        return m+n-2*self.lcs(word1,word2,m,n)

    
    def lcs(self,word1,word2,m,n):
        if m < 1 or n < 1:
            return 0
        a,b = (m-1),(n-1)
        if (a,b) in self.memo:
            return self.memo[(a,b)]
        if word1[a] == word2[b]:
            res =  1+self.lcs(word1,word2,a,b)
            self.memo[(a,b)] = res
        else:
            res = max(self.lcs(word1,word2,m-1,n),\
                       self.lcs(word1,word2,m,n-1))
            self.memo[(a,b)] = res
        return self.memo[(a,b)]


s = Solution()
print(s.minDistance("aaa","a"))
