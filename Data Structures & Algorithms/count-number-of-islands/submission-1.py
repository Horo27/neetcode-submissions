class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j):
            dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            grid[i][j] = "0"
            for l, c in dirs:
                nl, nc = i + l, j + c
                if 0 <= nl < len(grid) and 0 <= nc < len(grid[0]) and grid[nl][nc] == "1":
                    dfs(nl, nc)

        
        nr = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    nr += 1
        return nr

        