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
        intervals.sort()
        return all(x[1] <= y[0] for x, y in zip(intervals[:-1], intervals[1:]))


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
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

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

        return res


class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Sort intervals based on start time
        """
        intervals.sort(key=lambda x: x[0])

        # stores the end time of intervals
        rooms = []
        for x in intervals:
            if rooms and x[0] >= rooms[0]:
                # means two intervals can use the same room
                heapq.heapreplace(rooms, x[1])
            else:
                # a new room is allocated
                heapq.heappush(rooms, x[1])

        return len(rooms)


class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Very similar with what we do in real life. Whenever you want to start a meeting, 
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


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
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
