class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer!
        i = 0
        j = len(height) - 1
        
        water = 0
        
        while i < j :
            water = max(water, (j-i) * min(height[i], height[j])) # 현재 시점 기준 최대 물의 양은 저장하고
            if height[i] < height[j]: # 둘 중 더 작은 높이를 변화시키며 최대값 확인
                i += 1
            else:
                j -= 1
        return water
            
        
        