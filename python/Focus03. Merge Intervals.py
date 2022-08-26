class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        56. Merge Intervals
        1. Go through the intervals sorted by start 
        2. Combine the current interval with the previous one if they overlap, 
        3. Add it to the output by itself if they don't.
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
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        435. Non-overlapping Intervals (greedy alg)
        Return the minimum number of intervals you need to remove to make 
        the rest of the intervals non-overlapping.

        Heuristic: always pick the interval with the earliest end time. 
        Then you can get the max number of non-overlaps (or min number to remove). Reason: 
        the interval with the earliest end time produces the max capacity to hold rest intervals.
        E.g. Suppose current earliest end time of the rest intervals is x. Then available time slot left for other intervals is [x:]. If we choose another interval with end time y, then available time slot would be [y:]. Since x ≤ y, there is no way [y:] can hold more intervals then [x:]. Thus, the heuristic holds.

        Therefore, we can sort interval by ending time and keep track of current earliest end time. Once next interval's start time is earlier than current end time, then we have to remove one interval. Otherwise, we update earliest end time.
        """
        intervals.sort(key=lambda x: x[1])

        last, res = -inf, 0
        for x, y in intervals:
            # current start < previous end -> overlapping
            if x < last:
                res += 1
            else:
                last = y
        return res


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        57. Insert Interval
        Loop through the intervals [xi, yi] and compare with new interval [x0, y0]
        1) if yi < x0, add [xi, yi] to answer
        2) if y0 < xi, add [x0, y0] and the remaining of intervals to answer
        2) if overlapping, merge the two intervals 
            x0 = min(x0, xi) and y0 = max(y0, yi).
        """
        x0, y0 = newInterval
        res = []

        i, N = 0, len(intervals)
        while i < N:
            xi, yi = intervals[i]
            if y0 < xi:
                break
            if yi < x0:
                res.append([xi, yi])
            else:
                x0 = min(x0, xi)
                y0 = max(y0, yi)
            i += 1

        res.append([x0, y0])
        res.extend(intervals[i:])
        return res
