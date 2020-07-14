class Solution:
    def twoSum(self, nums, target):
        nums_set = set()
        for n in nums:
            if (target-n) in nums_set:
                self.ans.add((n,target-n,-target))
            nums_set.add(n)
        
    def threeSum(self, nums):
        nums.sort()
        self.ans = set()
        for idx,n in enumerate(nums):
            self.twoSum(nums[idx+1:],-n)
        return self.ans


s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
# nums = [0,0,0,0]
print(s.threeSum(nums))
