'''
-2 0 1 3
   ^  
     ^ 
       ^

'''

class Solution():
    def twoSumSmaller(self, l, nums, target):
        res = 0
        r = len(nums)-1
        while l < r:
            if (nums[l]+nums[r]) < target:
                res += r-l
                l += 1
            else:
                r -= 1
        return res
    
    def threeSumSmaller(self, nums, target):
        nums.sort()
        result = 0
        for i in range(0, len(nums)-2):
            result += self.twoSumSmaller(i+1, nums, target-nums[i])
        return result
    
s = Solution()
nums = [-2, 0, 1, 3]
target = 2
s.threeSumSmaller(nums, target)
