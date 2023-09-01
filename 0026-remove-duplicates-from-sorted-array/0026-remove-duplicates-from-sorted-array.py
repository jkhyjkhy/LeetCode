class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
         nums[:] = [nums[x] for x in range(len(nums)) if x==0 or nums[x] != nums[x-1]]