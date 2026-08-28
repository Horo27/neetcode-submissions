class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_ = 0
        from collections import deque

        def inBounds(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def bfs(i, j):
            dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            que = deque()
            que.append([i, j])
            grid[i][j] = 0
            area = 1
            while que:
                dim = len(que)
                for _ in range(dim):
                    [curr_lin, curr_col] = deque.popleft(que)
                    for lin, col in dirs:
                        next_lin, next_col = curr_lin + lin, curr_col + col
                        if inBounds(next_lin, next_col) and grid[next_lin][next_col] == 1:
                            que.append([next_lin, next_col])
                            grid[next_lin][next_col] = 0
                            area += 1
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_ = max(max_, bfs(i, j))
        return max_
                