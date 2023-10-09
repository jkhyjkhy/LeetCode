class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        index = []
        
        nums.sort()
        
        # -4, -1, -1, 0, 1, 2
        
        
        right = len(nums) - 1
        left = 0
        
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            
            if i>0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum == 0:
                    index.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1 # 포인터 이동
                    right -= 1
                    
                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
        
        return index
