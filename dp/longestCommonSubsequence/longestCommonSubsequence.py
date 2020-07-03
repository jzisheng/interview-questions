
class Solution():
    def longestCommonSubsequence(self,text1,text2):
        m,n = len(text1),len(text2)
        self.memo = {}
        return self.lcs(text1,text2,m,n)
    
    def lcs(self,text1,text2,m,n):
        if m <= 0 or n <= 0:
            return 0
        a,b = m-1,n-1
        if (a,b) in self.memo:
            return self.memo[(a,b)]
        elif text1[a] == text2[b]:
            res =  1+self.lcs(text1,text2,a,b)
            self.memo[(a,b)] = res
        else:
            res = max( self.lcs(text1,text2,m-1,n),\
                        self.lcs(text1,text2,m,n-1) )
            self.memo[(a,b)] = res
        return self.memo[(a,b)] 
    pass

s = Solution()
print(s.longestCommonSubsequence("abcde","ace"))
