class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 기존 코드의 최적화 버전
        
        result = []
        while matrix:
            result += matrix.pop(0)
            if not matrix:
                return(result)
            matrix = list(zip(*matrix))[::-1]
        
        