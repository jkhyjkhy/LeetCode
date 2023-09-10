class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k > len(nums):
            k = k%len(nums)
        stay_nums = nums[len(nums)-k:] 
        rotate_nums = nums[:len(nums)-k]
        
        nums[:] = list(stay_nums + rotate_nums) 
        
        """
        Do not return anything, modify nums in-place instead.
        """
        