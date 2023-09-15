class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = [0]*(len(citations)+1) # 배열을 만들고 모든 요소 초기화 
        # [0, 0, 0, 0, 0 ,,,]
        
        count = 1
        
        while count <= len(citations):
            for n in citations:
                if n >= count:
                    h_index[count] += 1
            count += 1
        
        for a in range(len(h_index), 0, -1):
            if a-1 <= h_index[a-1]:
                return a-1
        