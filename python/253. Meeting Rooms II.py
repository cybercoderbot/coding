"""
253. Meeting Rooms II
Medium

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        252. Meeting Rooms. True if could attend all meetings
        Sort time intervals by starting time
        Return True if no consecutive intervals overlap.
        """
        intervals.sort()
        return all(x[1] <= y[0] for x, y in zip(intervals[:-1], intervals[1:]))


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        253. Meeting Rooms II. Min number of rooms for all meetings
        Track the change of room numbers in time order.
        Save all time points and the change on current meeting rooms.
        Sort all the changes on the key of time points.
        Track the current number of using rooms cur and update result res.
        Time O(N*logN), Space O(N)
        """
        meetings = []
        for x in intervals:
            meetings.append((x[0], 1))
            meetings.append((x[1], -1))
        meetings.sort()

        rooms, res = 0, 0
        for x in meetings:
            rooms += x[1]
            res = max(res, rooms)
        return res


class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        253. Meeting Rooms II
        As in real life, whenever you want to start a meeting, 
        you go and check if any empty room available. If so take one of them. 
        Otherwise, you need to find a new room someplace else (res += 1).  
        After you finish the meeting, the room becomes available again (j += 1).

        Think about j as a pointer to the first available room. 
        """

        starts = sorted(x[0] for x in intervals)
        ends = sorted(x[1] for x in intervals)

        res, j = 0, 0
        for i in range(len(starts)):
            if starts[i] < ends[j]:
                res += 1
            else:
                j += 1
        return res
