class Solution:
    def lenoflongest(self, s, k):
        l = r = 0
        uniqC = 0
        maxLen = 0
        windowMap = {}
        while r < len(s):
            if s[r] not in windowMap:
                    uniqC += 1
            windowMap[s[r]] = windowMap.get(s[r], 0) + 1
            while uniqC > k and l < len(s):
                    windowMap[s[l]] -= 1
                    if windowMap[s[l]] == 0:
                            uniqC -= 1
                            del windowMap[s[l]]
                    l +=1
            r+=1
            maxLen = max(maxLen, r -l )
        return maxLen




s = Solution()
print(s.lenoflongest("eceba",2))
