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


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Loop through the intervals [xi, yi] and compare with new interval [x0, y0]
        1) if yi < x0, add [xi, yi] to answer
        2) if y0 < xi, add [x0, y0] and the remaining of intervals to answer
        2) if overlapping, merge the two intervals 
            x0 = min(x0, xi) and y0 = max(y0, yi)
        Time: O(N), Space: O(N)
        """
        i, N = 0, len(intervals)
        x0, y0 = newInterval

        res = []
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
