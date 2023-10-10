class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        index = []
        left = 0
        window = float('inf')
        
        if sum(nums) < target:
            return 0
        
        else:
            for right in range(len(nums)):
                target -= nums[right]
                while target <= 0:
                    window = min(window, right - left + 1) # 부분 배열의 크기 중 더 작은 것
                    target += nums[left]
                    left += 1
        
        return window