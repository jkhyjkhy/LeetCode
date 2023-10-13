class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidUnit(unit):
            unit = [char for char in unit if char != '.']
            return len(set(unit)) == len(unit) # 중복된게 없다면 True 있으면 길이가 달라지므로 False
        def isValidBox(board):
            for i in (0,3,6):
                for j in (0,3,6):
                    box = [board[x][y] for x in range(i,i+3) for y in range(j, j+3)]
                    if not isValidUnit(box):
                        return False
            return True
            
        def isValidRow(board):
            for row in board:
                if not isValidUnit(row):
                    return False
            return True
        
        def isValidCol(board):
            for i in range(0,9):
                col = [row[i] for row in board]
                if not isValidUnit(col):
                    return False
            return True
            
        
        return isValidBox(board) and isValidRow(board) and isValidCol(board)