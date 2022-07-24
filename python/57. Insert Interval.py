"""
57. Insert Interval
Medium

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


"""
Loop through the intervals [x, y] and compare with new interval [x0, y0]:

if y < x0, add [x, y] to answer;
if y0 < x, add [x0, y0] and the remaining of intervals to answer;
if overlapping, merge the two intervals x0 = min(x0, x) and y0 = max(y0, y).
Implementation (84ms, 45.46%):

Time complexity O(N)
Space complexity O(N)
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        i, N = 0, len(intervals)
        x2, y2 = newInterval
        res = []

        while i < N:
            x1, y1 = intervals[i]
            if y2 < x1:
                break

            if y1 < x2:
                res.append([x1, y1])
            else:
                x2, y2 = min(x2, x1), max(y2, y1)
            i += 1

        res.append([x2, y2])
        res.extend(intervals[i:])

        return res
