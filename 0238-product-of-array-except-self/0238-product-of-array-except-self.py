class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        
        left_parameter = 1
        for i in range(len(nums)):
            answer[i] *= left_parameter
            left_parameter *= nums[i]
            
        right_parameter = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= right_parameter
            right_parameter *= nums[i]
        
        return answer
        