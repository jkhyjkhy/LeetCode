class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string=""
        v=sorted(strs) # v를 오름차순으로 정렬, 사전식
        first = v[0]
        last = v[-1] # 사전식 정렬을 하면 첫 번째와 마지막 단어가 상대적으로 가장 관련이 멀도록 배치될것이므로
        for i in range(min(len(first), len(last))): # 둘 중 더 짧은 단어의 길이만큼 반복 검색
            if(first[i]!=last[i]):
                return string
            string+=first[i]
        return string