class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_ground = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    zero_ground.append([i, j])


        for i, j in zero_ground:
            for row in range(len(matrix)):
                matrix[row][j] = 0  # 열을 0으로 설정

            for col in range(len(matrix[0])):
                matrix[i][col] = 0  # 행을 0으로 설정
