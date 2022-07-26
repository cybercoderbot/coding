"""
252. Meeting Rooms
Easy

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """Sort intervals"""
        intervals.sort()
        # sorted(intervals, key=lambda x: x[0])
        return all(pre[1] <= nxt[0] for pre, nxt in zip(intervals[:-1], intervals[1:]))


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        return all(intervals[i-1][1] <= intervals[i][0] for i in range(1, len(intervals)))


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
