class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validRow(row):
            seen = set()
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in seen:
                        print("ceva")
                        return False
                    seen.add(board[row][col])
            return True
        
        def validCol(col):
            seen = set()
            for row in range(9):
                if board[row][col] != ".":  
                    if board[row][col] in seen:
                        print("altceva")
                        return False
                    seen.add(board[row][col])
            return True
        
        def validSquare(row, col):
            seen = set()
            for i in range(3):
                for j in range(3):
                    if board[row + i][col + j] != ".":
                        if board[row + i][col + j] in seen:
                            return False
                        seen.add(board[row + i][col + j])
            return True
        
        for i in range(9):
            if not validRow(i) or not validCol(i):
                print("aici", i)
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not validSquare(i, j):
                    print("aici", i, j)
                    return False
        return True

         