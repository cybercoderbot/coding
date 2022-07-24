"""
1893. Check if All the Integers in a Range Are Covered
Easy

You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.


Example 1:
Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: true
Explanation: Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.

Example 2:
Input: ranges = [[1,10],[10,20]], left = 21, right = 21
Output: false
Explanation: 21 is not covered by any range.
"""


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        merge = []
        for start, end in sorted(ranges):
            if merge and start <= merge[-1][1]+1:
                merge[-1][1] = max(merge[-1][1], end)
            else:
                merge.append([start, end])
        return any(x <= left <= right <= y for x, y in merge)


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = [0]*(right-left+1)
        for start, end in ranges:
            for x in range(start, end+1):
                if left <= x <= right:
                    covered[x - left] = 1
        return all(covered)


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cover = [False] * 51
        for start, end in ranges:
            for x in range(start, end+1):
                cover[x] = True
        return all(cover[x] for x in range(left, right+1))


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        vals = [0]*52
        for x, y in ranges:
            vals[x] += 1
            vals[y+1] -= 1
        prefix = 0
        for i, x in enumerate(vals):
            prefix += x
            if left <= i <= right and prefix == 0:
                return False
        return True
