class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 반시계로 돌려가며 pop(0)을 한다면
        
        result = []
        while matrix:
            spiral_matrix = matrix[0]
            matrix.pop(0)
            transposed = list(zip(*matrix))
            matrix = transposed[::-1]
            result += spiral_matrix
        
        return(result)