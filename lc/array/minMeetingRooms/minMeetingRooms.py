'''
[[0,  30], [5,  10], [15, 20]] 
20 30

'''
import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals: return 0
        intervals.sort(key=lambda x: x[0])
        meetingRooms = []
        heapq.heappush(meetingRooms, intervals[0][1])
        for start, end in intervals[1:]:
            if start >= meetingRooms[0]:
                heapq.heappop(meetingRooms)
            heapq.heappush(meetingRooms, end)
        return len(meetingRooms)

s = Solution()
intervals = [[0,  30], [5,  10], [15, 20]]
s.minMeetingRooms(intervals)
