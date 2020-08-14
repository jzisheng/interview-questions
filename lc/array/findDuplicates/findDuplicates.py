class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set()
        for n in nums:
            nums[abs(n)-1] *= -1
        for n in nums:
            if nums[abs(n)-1] > 0:
                res.add(abs(n))
                nums[abs(n)-1] *= -1
        return list(res)
