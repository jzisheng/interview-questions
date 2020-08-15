'''
[[1,2],[2,3],[3,4],[1,3]]
'''

def eraseOverlapIntervals( intervals):
    if not intervals: return 0
    intervals.sort()
    currEnd = intervals[0][1]
    res = 0
    i = 1
    while i < len(intervals):
        if currEnd > intervals[i][0]:
            res += 1
            currEnd = min(intervals[i][1], currEnd)
        else:
            currEnd = intervals[i][1]
        i += 1
    return res

arr = [[1,2],[2,3],[3,4],[1,3]]
arr = [[1,2],[1,2],[1,2]]
print(eraseOverlapIntervals(arr))
