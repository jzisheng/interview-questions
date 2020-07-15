'''
 0 1 1 2 2 2 2 3 3 3 3 3
 3 3 3 3 3 3 3 3 2 2 2 1
[0,1,0,2,1,0,1,3,2,1,2,1]
     1   1 2 1     1    

'''

class Solution:
    def trap(self, height):
        if len(height) < 1: return 0
        asc = [0]*len(height)
        desc = [0]*len(height)
        asc[0], desc[len(height)-1] = height[0], height[-1]


        for idx in range(1, len(height)):
            asc[idx] = max(asc[idx-1],height[idx])

        for idx in range(len(height)-2,-1,-1):
            desc[idx] = max(desc[idx+1],height[idx])


        res = 0
        for idx, h in enumerate(height):
            res += max(0, min(asc[idx], desc[idx]) - h)
        return res
        pass

s = Solution()
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
heights = [1,5]
s.trap(heights)

