class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        row_ele = [[0] * (n) for _ in range(n)]
        col_ele = [[0] * (n) for _ in range(n)]
        box_ele = [[0] * (n) for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    row_ele[i][int(board[i][j])-1] = 1
                    col_ele[j][int(board[i][j])-1] = 1
                    box_ele[(i//3)*3 + (j//3)][int(board[i][j])-1] = 1

        def helper(i, j):
            if i == n:
                return True
            if j == n:
                return helper(i+1, 0)

            if board[i][j] != ".":
                return helper(i, j + 1)

            for ele in range(1, 10): #ele
                if (not row_ele[i][ele-1]) and (not col_ele[j][ele-1]) and (not box_ele[(i//3)*3 + (j//3)][ele-1]):
                    board[i][j] = str(ele)
                    row_ele[i][ele-1] = 1
                    col_ele[j][ele-1] = 1
                    box_ele[(i//3)*3 + (j//3)][ele-1] = 1
                        
                    if helper(i, j+1):
                        return True

                    row_ele[i][ele-1] = 0
                    col_ele[j][ele-1] = 0
                    box_ele[(i//3)*3 + (j//3)][ele-1] = 0
                    board[i][j] = "."

            return False

        helper(0, 0)
            
