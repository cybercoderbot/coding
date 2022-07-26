class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 解题思路：递归（Recursion）DFS
        # 记传入数组为nums，若nums的长度不大于1，则直接返回[nums]
        # 遍历nums，从中抽取一个数num，递归计算剩余数字组成的数组n，然后将num与结果合并

        if len(nums) <= 1:
            return [nums]
        ans = []

        for i, n in enumerate(nums):
            num = nums[:i] + nums[i+1:]
            for pm in self.permute(num):
                ans.append([n] + pm)

        return ans
