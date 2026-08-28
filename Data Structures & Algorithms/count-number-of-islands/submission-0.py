class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque

        def bfs(i, j):
            dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            que = deque()
            que.append([i, j])
            grid[i][j] = "0"

            while que:
                dim = len(que)
                for _ in range(dim):
                    [cl, cc] = deque.popleft(que)
                    for lin, col in dirs:
                        nl, nc = lin + cl, col + cc
                        if 0 <= nl < len(grid) and 0 <= nc < len(grid[0]) and grid[nl][nc] == "1":
                            grid[nl][nc] = "0"
                            que.append([nl, nc])
        
        nr = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    nr += 1
        return nr

        