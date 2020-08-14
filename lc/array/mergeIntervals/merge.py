class Solution:
    def inInterval(self, a, b):
        if a[1] < b[0]:
            return False
        return True
    
    def merge(self, intervals):
        if not(intervals):
            return None
        intervals.sort(key=lambda x: x[0])
        res = [intervals.pop(0)]
        while intervals:
            if self.inInterval(res[-1], intervals[0]):
                res[-1][1] = max(res[-1][1], intervals[0][1])
                intervals.pop(0)
            else:
                res.append(intervals.pop(0))
        return res
        pass


s = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
#intervals = [[1,2]]
s.merge(intervals)
