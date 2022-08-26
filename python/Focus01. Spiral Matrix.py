class Solution:
    def matrixReshape(self, mat: List[List[int]], R: int, C: int) -> List[List[int]]:
        """
        566. Reshape the Matrix
        """
        M, N = len(mat), len(mat[0])
        if M * N != R * C:
            return mat

        reshaped = [[None] * C for _ in range(R)]

        for i in range(M * N):
            reshaped[i//C][i % C] = mat[i//N][i % N]
        return reshaped


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        867. Transpose Matrix
        """
        M, N = len(matrix), len(matrix[0])
        trans = [[0]*M for _ in range(N)]
        for i, j in product(range(M), range(N)):
            trans[j][i] = matrix[i][j]
        return trans


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        73. Set Matrix Zeroes
        If an element == 0, set its entire row and col to 0.
        """
        if not matrix:
            return []

        M, N = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        for i, j in product(range(M), range(N)):
            if not matrix[i][j]:
                rows.add(i)
                cols.add(j)

        for i, j in product(range(M), range(N)):
            if i in rows or j in cols:
                matrix[i][j] = 0
        return


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        74. Search a 2D Matrix
        """
        M, N = len(matrix), len(matrix[0])

        low, high = 0, M * N
        while low < high:
            mid = (low + high) // 2
            i, j = divmod(mid, N)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                low = mid + 1
            else:
                high = mid

        return False


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        """
        562. Longest Line of Consecutive One in Matrix
        Return the length of the longest consecutive 0's in the matrix.
        """
        if not mat:
            return 0

        res = 0
        M, N = len(mat), len(mat[0])
        rows, cols = [0]*M, [0]*N
        diag1, diag2 = [0]*(M+N-1), [0]*(M+N-1)
        for i, j in product(range(M), range(N)):
            if mat[i][j]:
                rows[i] += 1
                cols[j] += 1
                diag1[j-i+M-1] += 1
                diag2[i+j] += 1
            else:
                rows[i] = cols[j] = diag1[j-i+M-1] = diag2[i+j] = 0
            res = max(res, rows[i], cols[j], diag1[j-i+M-1], diag2[i+j])
        return res


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        766. Toeplitz Matrix
        A matrix is Toeplitz if every diagonal from top-left to bottom-right
        has the same elements.
        """
        M, N = len(matrix), len(matrix[0])
        for i, j in product(range(M-1), range(N-1)):
            if matrix[i+1][j+1] != matrix[i][j]:
                return False
        return True


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        766. Toeplitz Matrix
        """
        M, N = len(matrix), len(matrix[0])
        grids = product(range(M-1), range(N-1))
        return all(matrix[i+1][j+1] == matrix[i][j] for i, j in grids)


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        1572. Matrix Diagonal Sum
        """
        N = len(mat)
        mid = N // 2
        res = 0
        for i in range(N):
            res += mat[i][i]
            res += mat[N-1-i][i]
        if N % 2:
            res -= mat[mid][mid]
        return res


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        """
        1380. Lucky Numbers in a Matrix
        A lucky number in the matrix is the element that's the min in its row
        and max in its column.
        """
        low, high = set(), set()

        for row in matrix:
            low.add(min(row))

        for col in zip(*matrix):
            high.add(max(col))

        return list(low & high)


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        """
        1380. Lucky Numbers in a Matrix
        """
        transposed = zip(*matrix)
        low = set(min(row) for row in matrix)
        high = set(max(col) for col in transposed)
        return list(low & high)


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        311. Sparse Matrix Multiplication
        """
        M, K, N = len(A), len(B), len(B[0])
        res = [[0] * N for _ in range(M)]
        for i, k in product(range(M), range(K)):
            if not A[i][k]:
                continue
            for j in range(N):
                if not B[k][j]:
                    continue
                res[i][j] += A[i][k] * B[k][j]
        return res


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        542. 01 Matrix
        Return the distance of the nearest 0 for each cell.
        """
        M, N = len(mat), len(mat[0])
        queue = collections.deque([])
        seen = set()
        for i, j in product(range(M), range(N)):
            if not mat[i][j]:
                queue.append((i, j, 0))
                seen.add((i, j))

        res = [[0]*N for _ in range(M)]
        while queue:
            i, j, depth = queue.popleft()
            res[i][j] = depth
            for x, y in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                if not (0 <= x < M and 0 <= y < N):
                    continue
                if (x, y) not in seen:
                    seen.add((x, y))
                    queue.append((x, y, depth+1))
        return res


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        1314. Matrix Block Sum
        """
        M, N = len(mat), len(mat[0])
        csum = [[0]*(N+1) for _ in range(M+1)]

        for i, j in product(range(M), range(N)):
            csum[i+1][j+1] = csum[i][j+1] + \
                csum[i+1][j] + mat[i][j] - csum[i][j]

        res = [[0]*N for _ in range(M)]
        for i, j in product(range(M), range(N)):
            r0, r1 = max(0, i-k), min(M-1, i+k)
            c0, c1 = max(0, j-k), min(N-1, j+k)
            res[i][j] = csum[r1+1][c1+1] - csum[r0][c1+1] - \
                csum[r1+1][c0] + csum[r0][c0]
        return res


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        1329. Sort the Matrix Diagonally
        """
        M, N = len(mat), len(mat[0])
        diags = collections.defaultdict(list)
        for i, j in product(range(M), range(N)):
            diags[i-j].append(mat[i][j])

        for d in diags.values():
            d.sort(reverse=False)

        res = [[0] * N for _ in range(M)]
        for i, j in product(range(M), range(N)):
            res[i][j] = diags[i-j].pop(0)
        return res


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """
        1605. Find Valid Matrix Given Row and Column Sums
        Greedy algorithm
        """
        M, N = len(rowSum), len(colSum)
        res = [[0] * N for i in range(M)]
        for i, j in product(range(M), range(N)):
            res[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= res[i][j]
            colSum[j] -= res[i][j]
        return res


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        54. Spiral Matrix
        Time complexity O(MN)
        Return all elements of the matrix in spiral order.
        """
        i = j = 0
        di, dj = 0, 1
        M, N = len(matrix), len(matrix[0])
        nums = []
        for _ in range(M * N):
            nums.append(matrix[i][j])
            matrix[i][j] = None
            if not matrix[(i+di) % M][(j+dj) % N]:
                di, dj = dj, -di
            i += di
            j += dj
        return nums


class Solution:
    def generateMatrix(self, N: int) -> List[List[int]]:
        """
        59. Generate Spiral Matrix II
        Generate an N x N matrix filled with elements from 1 to N^2 in spiral order.
        """
        mat = [[None]*N for _ in range(N)]
        i = j = 0
        di, dj = 0, 1
        for x in range(1, N*N+1):
            mat[i][j] = x
            if mat[(i+di) % N][(j+dj) % N]:
                di, dj = dj, -di
            i += di
            j += dj
        return mat


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        54. Traverse Spiral Matrix
        """
        M, N = len(matrix), len(matrix[0])
        i, j, k = 0, 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        di, dj = directions[k]
        nums = []
        for _ in range(M * N):
            nums.append(matrix[i][j])
            matrix[i][j] = None
            if not matrix[(i+di) % M][(j+dj) % N]:
                k += 1
                di, dj = directions[k % 4]
            i += di
            j += dj

        return nums


class Solution:
    def generateMatrix(self, N: int) -> List[List[int]]:
        """
        59. Generate Spiral Matrix II
        """
        mat = [[None]*N for _ in range(N)]
        i, j, k = 0, 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        di, dj = directions[k]
        for x in range(1, N*N+1):
            mat[i][j] = x
            if mat[(i+di) % N][(j+dj) % N]:
                k += 1
                di, dj = directions[k % 4]
            i += di
            j += dj
        return mat


class Solution:
    def spiralMatrix(self, M: int, N: int, head: Optional[ListNode]) -> List[List[int]]:
        """
        2326. Spiral Matrix IV
        Construct spiral matrix from linked list
        """
        node = head
        res = [[-1]*N for _ in range(M)]
        i, j = 0, 0
        di, dj = 0, 1
        while node:
            res[i][j] = node.val
            node = node.next
            if res[(i+di) % M][(j+dj) % N] != -1:
                di, dj = dj, -di
            i += di
            j += dj
        return res


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        378. Kth Smallest Element in a Sorted Matrix
        """
        N = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]

        def check(x):
            """Return number of elements <= x"""
            i, j = 0, N-1
            count = 0
            for i in range(N):
                while j >= 0 and matrix[i][j] > x:
                    j -= 1
                count += (j + 1)
            return count

        while left < right:
            mid = (left + right) // 2
            if check(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        329. Longest Increasing Path in a Matrix
        """
        M, N = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(i, j):
            """Return max increasing path starting from (i, j)."""
            res = 1
            for x, y in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                if 0 <= x < M and 0 <= y < N and matrix[x][y] > matrix[i][j]:
                    res = max(res, dfs(x, y) + 1)
            return res

        return max(dfs(i, j) for i in range(M) for j in range(N))


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, r0: int, c0: int) -> List[List[int]]:
        """
        885. Spiral Matrix III
        Return an array of coordinates in the order you visited them starting at (r0, c0)
        """
        i, j = r0, c0
        res = [[r0, c0]]
        di, dj = 0, 1
        turns, length = 0, 1
        while len(res) < rows * cols:
            for _ in range(length):
                i, j = i + di, j + dj
                if 0 <= i < rows and 0 <= j < cols:
                    res.append([i, j])
            di, dj = dj, -di
            if turns % 2:
                length += 1
            turns += 1
        return res


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, r0: int, c0: int) -> List[List[int]]:
        """
        885. Spiral Matrix III
        """
        i, j = r0, c0
        res = [[r0, c0]]
        length, sign = 1, 1
        while len(res) < rows * cols:
            for _ in range(length):
                j += sign
                if 0 <= i < rows and 0 <= j < cols:
                    res.append([i, j])

            for _ in range(length):
                i += sign
                if 0 <= i < rows and 0 <= j < cols:
                    res.append([i, j])
            length += 1
            sign *= -1
        return res
