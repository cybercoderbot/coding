class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        252. Meeting Rooms
        True if a person could attend all meetings.
        """
        intervals.sort()
        return all(x[1] <= y[0] for x, y in zip(intervals[:-1], intervals[1:]))


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        253. Meeting Rooms II
        """
        meetings = []
        for start, end in intervals:
            meetings.append((start, 1))
            meetings.append((end, -1))

        meetings.sort()

        rooms, res = 0, 0
        for mt in meetings:
            rooms += mt[1]
            res = max(res, rooms)
        return res


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        1094. Car Pooling
        """
        occupancy = []
        for x, src, dst in trips:
            occupancy.append((src, x))
            occupancy.append((dst, -x))

        occupancy.sort()

        passengers = 0
        for occu in occupancy:
            passengers += occu[1]
            if passengers > capacity:
                return False
        return True


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], N: int) -> List[int]:
        """
        1109. Corporate Flight Bookings
        """
        res = [0] * N
        flights = []
        for first, last, x in bookings:
            flights.append((first-1, x))
            flights.append((last, -x))

        flights.sort()

        pre, seats = 0, 0
        for i, x in flights:
            for j in range(pre, i):
                res[j] += seats
            pre = i
            seats += x
        return res


class MyCalendar:
    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        """
        729. My Calendar I (no double booking)
        """
        for x, y in self.calender:
            if start < y and end > x:
                return False
        self.calender.append((start, end))
        return True


class MyCalendarTwo:
    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        """
        731. My Calendar II (no triple booking)
        [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
        """
        for x, y in self.overlaps:
            if start < y and end > x:
                return False
        for x, y in self.calendar:
            if start < y and end > x:
                self.overlaps.append((max(start, x), min(end, y)))
        self.calendar.append((start, end))
        return True


class MyCalendarTwo:
    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        """
        731. My Calendar II (no triple booking)
        [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
        """
        self.calender.append((start, +1))
        self.calender.append((end, -1))
        self.calender.sort()

        overlaps = 0
        for book in self.calender:
            overlaps += book[1]
            if overlaps > 2:
                # remove the booking that is causing triple overlap
                self.calender.remove((start, +1))
                self.calender.remove((end, -1))
                return False

        return True


class MyCalendarThree:
    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> int:
        """
        732. My Calendar III
        Return the maximum k-booking between all the previous events
        """
        self.bookings.append((start, end))

        calender = []
        for start, end in self.bookings:
            calender.append((start, +1))
            calender.append((end, -1))
        calender.sort()

        res, overlaps = 0, 0
        for cal in calender:
            overlaps += cal[1]
            res = max(res, overlaps)
        return res


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        """
        1229. Meeting Scheduler
        Return the earliest time that works for both with duration
        """
        slots1.sort()
        slots2.sort()
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            if start + duration <= end:
                return [start, start + duration]
            if slots1[i][1] <= slots2[j][1]:
                i += 1
            else:
                j += 1
        return []


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        56. Merge Intervals (merge all overlapping intervals)
        1. Go through the intervals sorted by start
        2. Combine the current interval with the previous one if they overlap,
        3. Add it to the output by itself if they don't.
        intervals = [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        for x, y in intervals[1:]:
            if x <= res[-1][1]:
                # [[1,4], [4,5]] -> [1,5]
                res[-1][1] = max(y, res[-1][1])
            else:
                res.append([x, y])

        return res


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """
        759. Employee Free Time
        class Interval:
            def __init__(self, start: int = None, end: int = None):
                self.start = start
                self.end = end
        """
        intervals = sorted([[t.start, t.end] for s in schedule for t in s])
        # intervals = sorted([t for s in schedule for t in s], key=lambda x: x.start)
        res = []
        last = intervals[0][-1]
        for x in intervals[1:]:
            if x[0] > last:
                res.append(Interval(last, x[0]))
            last = max(last, x[-1])
        return res
