'''
Dutch flag problem

[0,0,2,1,1,2]
     ^         
       ^
'''

class Solution:
    def sortColors(self, nums):
        l, r = 0, len(nums)-1
        curr = 0
        while curr <= r:
            if nums[curr] == 0:
                nums[l], nums[curr] = nums[curr], nums[l]
                curr += 1
                l += 1
            elif nums[curr] == 2:
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1
            elif nums[curr] == 1:
                curr += 1
        pass


s = Solution()
nums = [2,0,2,1,1,0]
s.sortColors(nums)
print(nums)
