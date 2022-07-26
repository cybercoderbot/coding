class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # 解题思路：
        # 初始对角线方向为右上方（偏移量：行-1, 列+1）
        # 遇到边界时转向左下方（偏移量：行+1, 列-1）

        # 对于边界的处理：
        # 向右上方移动遇到上边界时，若未达到右边界，则向右移动（偏移量：行+0，列+1），否则向下移动（偏移量：行+1，列+0）
        # 向左下方移动遇到左边界时，若未达到下边界，则向下移动（偏移量：行+1，列+0），否则向右移动（偏移量：行+0，列+1）

        if not matrix:
            return []
        i, j, k = 0, 0, 1
        w, h = len(matrix), len(matrix[0])
        ans = []
        for x in range(w * h):
            ans.append(matrix[i][j])
            # move towards right
            if k == 1:
                di, dj = i - 1, j + 1
            else:
                di, dj = i + 1, j - 1
            if 0 <= di <= w-1 and 0 <= dj <= h-1:
                i, j = di, dj
            else:
                if k > 0:
                    if j + 1 < h:
                        j += 1
                    else:
                        i += 1
                else:
                    if i + 1 < w:
                        i += 1
                    else:
                        j += 1
                k *= -1
        return ans
