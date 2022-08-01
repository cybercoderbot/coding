"""
252. Meeting Rooms
Easy

Given an array of meeting time intervals where intervals[i] = [start, end],
determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
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
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        252. Meeting Rooms. True if could attend all meetings
        Sort time intervals by starting time
        Return True if no consecutive intervals overlap.
        """
        intervals.sort()
        return all(intervals[i-1][1] <= intervals[i][0] for i in range(1, len(intervals)))


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
        253. Meeting Rooms II. Min number of rooms for all meetings
        Sort time intervals by starting time
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        rooms = [intervals[0][1]]
        for x in intervals[1:]:
            if x[0] >= rooms[-1]:
                rooms.pop()
            rooms.append(x[1])
            rooms.sort(reverse=True)
        return len(rooms)


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> int:

        # intervals: [[0,30],[5,10],[15,20]]
        # s: [(0, 'start'), (30, 'end'), (5, 'start'), (10, 'end'), (15, 'start'), (20, 'end')]

        meetings = []
        for start, end in intervals:
            meetings.append((start, "start"))
            meetings.append((end, "end"))

        meetings.sort()
        # meetings = sorted(intervals, key=lambda x: x[0])
        # s: [(0, 'start'), (5, 'start'), (10, 'end'), (15, 'start'), (20, 'end'), (30, 'end')]

        count, res = 0, 0
        for _, flag in meetings:
            if flag == "start":
                count += 1
                res = max(res, count)
            elif flag == "end":
                count -= 1

        return res == 1
