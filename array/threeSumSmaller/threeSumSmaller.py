'''
targetTwoSum = 2 - (-2)
              target-nums[i]
  -2 0 1 3
i  ^
l    ^
r        ^

'''

class Solution():
    def twoSumSmaller(self, l, nums, target):
        res = 0
        r = len(nums)-1
        while l < r:
            if nums[l] + nums[r] < target:
                res += r-l
                l += 1
            else:
                r -= 1
            pass
        return res
    
    def threeSumSmaller(self, nums, target):
        nums.sort()
        res = 0
        for i in range(0, len(nums)-2):
            res += self.twoSumSmaller(i+1, nums, target-nums[i])
        return res
        pass
    
s = Solution()
nums = [-2, 0, 1, 3]
target = 2
s.threeSumSmaller(nums, target)
