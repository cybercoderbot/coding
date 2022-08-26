class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        """
        490. The Maze
        """
        M, N = len(maze), len(maze[0])
        queue = collections.deque([start])
        seen = {tuple(start)}
        while queue:
            r, c = queue.popleft()
            if [r, c] == destination:
                return True
            for di, dj in (-1, 0), (0, -1), (0, 1), (1, 0):
                i, j = r, c
                while 0 <= i+di < M and 0 <= j+dj < N and not maze[i+di][j+dj]:
                    i += di
                    j += dj
                if (i, j) not in seen:
                    queue.append((i, j))
                    seen.add((i, j))
        return False


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        """
        505. The Maze II
        """
        M, N = len(maze), len(maze[0])
        # min-heap
        heap = [(0, start[0], start[1])]
        dist = defaultdict(lambda: inf, {tuple(start): 0})

        while heap:
            x0, r, c = heappop(heap)
            if [r, c] == destination:
                return x0
            for di, dj in (-1, 0), (0, -1), (0, 1), (1, 0):
                i, j = r, c
                while 0 <= i+di < M and 0 <= j+dj < N and not maze[i+di][j+dj]:
                    i += di
                    j += dj
                x = x0 + abs(i - r) + abs(j - c)
                if x < dist[i, j]:
                    heappush(heap, (x, i, j))
                    dist[i, j] = x
        return -1


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        """
        499. The Maze III
        """
        M, N = len(maze), len(maze[0])
        heap = [(0, "", ball[0], ball[1])]
        stopped = {(ball[0], ball[1]): [0, ""]}

        while heap:
            dist, pattern, r, c = heapq.heappop(heap)
            if [r, c] == hole:
                return pattern
            for di, dj, p in (-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r"):
                i, j, d = r, c, 0
                while 0 <= i+di < M and 0 <= j+dj < N and maze[i+di][j+dj] != 1:
                    i += di
                    j += dj
                    d += 1
                    if [i, j] == hole:
                        break
                if (i, j) not in stopped or [dist+d, pattern+p] < stopped[(i, j)]:
                    stopped[(i, j)] = [dist+d, pattern+p]
                    heapq.heappush(heap, (dist+d, pattern+p, i, j))
        return "impossible"
