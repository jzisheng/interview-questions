'''
  1,4,3,7,5,2,6,5,4,8,5,6
l ^
r ^

start l r = 0
windowMax = 0
while l < len(N) and r < len(N):
if every element in window should be as big as r-l
  windowMax = max(windowMax, r-l)
  r += 1
else
  l += 1

'''

class Solution:    
    def largestSquareArea(self, heights):
        if len(heights) <= 1:
            return 0
        l,r = 0,1
        res = 0
        while l < len(heights) and r < len(heights):
            if any(x < r-l for x in heights[l:r]):
                l += 1
            else:
                r += 1
            res = max(res, r-l)
        return res
    
    def largestRectangleArea(self, heights):
        pass


s = Solution()
heights = [1,4,3,7,5,2,6,5,4,8,5,6]
print(s.largestSquareArea(heights))
