class Solution():
    def findDuplicate(self, nums):
        t, h = nums[0], nums[0]
        # keep going until tort and hare intersect
        while True:
            t = nums[t]
            h = nums[nums[h]]
            if t == h: break

        t = nums[0]
        while t != h:
            t = nums[t]
            h = nums[h]
        return h


s = Solution()
nums = [1,3,4,2,2]
s.findDuplicate(nums)
