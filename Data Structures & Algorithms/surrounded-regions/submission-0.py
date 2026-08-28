class Solution:
    def solve(self, board: List[List[str]]) -> None:
        from collections import deque
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def inBounds(i, j):
            return 0 <= i < len(board) and 0 <= j <len(board[0])

        def bfs(i, j):
            que = deque()
            que.append([i, j])
            board[i][j] = "S"

            while que:
                dim = len(que)
                for _ in range(dim):
                    [ci, cj] = deque.popleft(que)
                    for i, j in dirs:
                        ni, nj = ci + i, cj + j
                        if inBounds(ni, nj) and board[ni][nj] == 'O':
                            que.append([ni, nj])
                            board[ni][nj] = "S"

        for i in range(len(board)):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][len(board[0]) - 1] == "O":
                bfs(i, len(board[0]) - 1)

        for i in range(len(board[0])):
            if board[0][i] == 'O':
                bfs(0, i)
            if board[len(board) - 1][i] == "O":
                bfs(len(board) - 1, i)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

