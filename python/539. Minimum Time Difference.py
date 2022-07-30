"""
539. Minimum Time Difference
Medium

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0"""


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        MIN_PER_HOUR, HOURS = 60, 24
        MIN_PER_DAY = MIN_PER_HOUR * HOURS

        def timeInMinutes(time):
            """Return time point as minute."""
            nonlocal MIN_PER_HOUR
            h, m = map(int, time.split(":"))
            return MIN_PER_HOUR * h + m

        # times = sorted(map(timeInMinutes, timePoints))
        times = sorted(timeInMinutes(t) for t in timePoints)

        times += [times[0]]
        diffs = [(y-x) % MIN_PER_DAY for x, y in zip(times[:-1], times[1:])]

        return min(diffs)


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        Sort: convert time in timePoints into a sorted list then find the min difference
        between the two neighbors. Remember to compare the biggest one with the smallest as the example shows.

        Time: O(N logN)

        """

        MIN_PER_HOUR, HOURS = 60, 24
        MIN_PER_DAY = MIN_PER_HOUR * HOURS

        def timeInMinutes(time):
            nonlocal MIN_PER_HOUR
            hour, minute = map(int, time.split(":"))
            return hour * MIN_PER_HOUR + minute

        times = sorted(timeInMinutes(t) for t in timePoints)

        res = MIN_PER_DAY
        for i in range(1, len(times)):
            res = min(res, times[i] - times[i-1])

        # ["23:59","00:00"] -> -1439, expected 1
        return min(MIN_PER_DAY + times[0] - times[-1], res)


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        MIN_PER_HOUR, HOURS = 60, 24
        MIN_PER_DAY = MIN_PER_HOUR * HOURS

        # sorting
        timePoints = sorted(
            MIN_PER_HOUR * int(x[:2]) + int(x[3:]) for x in timePoints)
        timePoints += [timePoints[0]]

        return min((timePoints[i] - timePoints[i-1]) % MIN_PER_DAY for i in range(1, len(timePoints)))
