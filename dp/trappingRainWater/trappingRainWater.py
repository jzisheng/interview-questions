import collections
class Solution:  
    def trap(self, height):
        if not height: return 0
        maxLeft = [0]*len(height)
        maxLeft[0] = height[0]
        maxRight = [0]*len(height)
        maxRight[len(height)-1] = height[-1]
        
        for i in range(1,len(height)):
            maxLeft[i] = max(maxLeft[i-1],height[i])

        for i in range(len(height)-2,-1,-1):
            maxRight[i] = max(maxRight[i+1],height[i])
            pass

        volume = 0
        for i in range(len(height)):
            if height[i] < maxLeft[i] and height[i] < maxRight[i]:
                volume += min(maxLeft[i],maxRight[i])-height[i]
        return volume
    pass

print("")
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print(s.trap(heights))
