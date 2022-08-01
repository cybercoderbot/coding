"""
274. H-Index
Medium

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.

Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more
than 3 citations each, their h-index is 3.

Example 2:
Input: citations = [1,3,1]
Output: 1
"""


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sort = sorted(citations, reverse=True)
        return sum(i < x for i, x in enumerate(sort))


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sort = sorted(citations, reverse=True)
        return max((i+1 for i, x in enumerate(sort) if i < x), default=0)


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sort = sorted(citations, reverse=True)
        return max((min(i, x) for i, x in enumerate(sort, 1)), default=0)


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """274. H-Index. Sort citations -> Two pointers"""
        citations.sort()
        N = len(citations)
        left, right = 0, N
        while left < right:
            mid = (left + right) // 2
            if citations[mid] >= N - mid:
                right = mid
            else:
                left = mid + 1
        return N - left


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """275. H-Index. Citations sorted. Two pointers"""
        N = len(citations)
        left, right = 0, N
        while left < right:
            mid = (left + right)//2
            if citations[mid] >= N - mid:
                right = mid
            else:
                left = mid + 1
        return N - left
