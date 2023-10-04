class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index = {}
        
        for i, a in enumerate(numbers):
            remains = target - a
            
            if remains in index:
                return [index[remains]+1, i+1]
            index[a] = i