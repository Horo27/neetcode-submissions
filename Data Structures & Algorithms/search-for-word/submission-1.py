class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(lin, col, pos, seen):
            print(pos)

            if pos == len(word):
                return True
            
            for i, j in dirs:
                nlin = lin + i
                ncol = col + j

                if 0 <= nlin < len(board) and 0 <= ncol < len(board[0]):
                    if board[nlin][ncol] == word[pos] and (nlin, ncol) not in seen:
                        seen.add((nlin, ncol))
                        found = dfs(nlin, ncol, pos + 1, seen)
                        seen.remove((nlin, ncol))

                        if found:
                            return True
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1, {(i, j)}):
                        return True
        return False