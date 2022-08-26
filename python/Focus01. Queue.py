class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        """
        364. Nested List Weight Sum II
        nestedList = [1,[4,[6]]] -> 1*3 + 4*2 + 6*1 = 17
        """
        res = val = 0
        queue = nestedList
        while queue:
            newq = []
            for x in queue:
                if x.isInteger():
                    val += x.getInteger()
                else:
                    newq.extend(x.getList())
            res += val
            queue = newq
        return res


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.idx = 0
        self.nums = self.flatten(nestedList)

    def flatten(self, nestedList: [NestedInteger]) -> List[int]:
        """341. Flatten Nested List Iterator"""
        nums = []
        for x in nestedList:
            if x.isInteger():
                nums.append(x.getInteger())
            else:
                nums.extend(self.flatten(x.getList()))
        return nums

    def next(self) -> int:
        nxt = self.nums[self.idx]
        self.idx += 1
        return nxt

    def hasNext(self) -> bool:
        return self.idx < len(self.nums)
