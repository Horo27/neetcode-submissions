class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        que = deque()
        fresh = 0
        minutes = 0
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    que.append([i, j])
        
        while que and fresh:
            dim = len(que)
            for _ in range(dim):
                [ci, cj] = deque.popleft(que)
                for i, j in dirs:
                    ni, nj = ci + i, cj + j
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                        fresh -= 1
                        grid[ni][nj] = 2
                        que.append([ni, nj])
            minutes += 1
        
        if fresh:
            return -1
        return minutes