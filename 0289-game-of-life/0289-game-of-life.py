class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        future_board = [[0] * len(board[0]) for _ in range(len(board))]


        for row in range(len(board)):
            for col in range(len(board[0])):
                count = 0
                for nr, nc in neighbors: # 이웃의 상태를 점검

                    r, c = row + nr, col + nc
                    if 0 <= r < len(board) and 0 <= c < len(board[0]): # 이웃이 셀 위에 실존하는 이웃인지 확인
                        count += board[r][c]

                if not board[row][col]: # 현재 셀이 죽은 셀
                    if count == 3:
                        future_board[row][col] = 1
                    else:
                        future_board[row][col] = 0

                else: # 현재 셀이 살아 있는 셀
                    if count < 2 or count > 3:
                        future_board[row][col] = 0
                    else:
                        future_board[row][col] = 1
        board[:] = future_board
