"""
56. Merge Intervals
Medium


Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Solution:

Just go through the intervals sorted by start coordinate and either combine the current interval with the 
previous one if they overlap, or add it to the output by itself if they don't.

"""            


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0: 
            return []
        
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        for pair in intervals[1:]:
            if pair[0] <= res[-1][1]: 
                # [[1,4], [4,5]] -> [1,5]
                res[-1][1] = max(pair[1], res[-1][1])
            else: 
                res.append(pair)
                
        return res