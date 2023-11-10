class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        cur_count = 1 # 현재 카운트
        max_count = 1 # 연속되는 숫자가 있다면 최대 카운트는 무조건 1보다 크므로 
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                cur_count+=1 # 연속된다면 현재 카운트 계속 늘리기
            elif nums[i] == nums[i-1]:
                continue
            else:
                max_count = max(cur_count,max_count)
                cur_count = 1
            
        return max(max_count, cur_count)