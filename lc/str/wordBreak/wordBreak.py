class Solution:
    def f(self,s,i):
        print("====== "+s)
        if i == len(s):
            return True
        if i in self.memo:
            return self.memo[i]
        for j in range(i,len(s)):
            print(s[i:j])            
            if s[i:j] in self.wordMap and self.f(s[j:], j):
                
                self.memo[i] = True
                return self.memo[i]
        self.memo[i] = False
        return self.memo[i]
    
    def wordBreak(self, s, wordDict):
        self.memo = {}
        self.wordMap = set()
        for w in wordDict:
            self.wordMap.add(w)
        return self.f(s,0)
        pass

sol = Solution()
s = "applepenapple"
wordDict = ["apple","pen"]
print(sol.wordBreak(s, wordDict))
