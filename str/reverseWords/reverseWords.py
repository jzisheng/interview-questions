class Solution:
    def reverseStr(self, S, l, r):
        while l < r:
            S[l], S[r] = S[r], S[l]
            l, r = l+1, r-1
        pass

    def reverseEachWord(self, s):
        n = len(s)
        start = end = 0
        while start < n:
            while end < n and s[end] != ' ':
                end += 1
            self.reverseStr(s, start, end-1)
            start = end + 1
            end += 1
    
    def reverseWords(self, s):
        self.reverseStr(s, 0, len(s)-1)
        self.reverseEachWord(s)
        pass
    pass


ss = Solution()
words = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
words = [' ', 'a']
ss.reverseWords(words)
print(words)
