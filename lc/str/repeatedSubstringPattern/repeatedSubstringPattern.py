'''
"abcabcabcabc"
            ^
'''

class Solution:
    def repeatedSubstringPattern(self, s):
        valid = False
        for w in range(1,(len(s)//2)+1):
            prev = None
            for i in range(0,len(s),w):
                ss = s[i:i+w]
                if prev == None:
                    prev = ss
                elif ss != prev:
                    valid = False
                    break
                else:
                    valid = True
            if valid and (i+w) == len(s):
                return True
        return False

pass
s = "abcabcab"
sol = Solution()
print(sol.repeatedSubstringPattern(s))
