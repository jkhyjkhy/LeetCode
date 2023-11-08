class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {} # 딕셔너리 선언
        
        for index, value in enumerate(nums):
            if value in seen and abs(index-seen[value]) <= k:
                return True
            else:
                seen[value] = index
        return False
        
        
                
