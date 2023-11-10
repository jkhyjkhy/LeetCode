class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        current_range = []
        start_index = 0
        if len(nums) == 1:
            ranges.append(rangesToString(nums[0],nums[0]))
            return ranges
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                if i == len(nums)-1: # 순회가 끝나면
                    ranges.append(rangesToString(nums[start_index], nums[i]))
                continue
            else:
                ranges.append(rangesToString(nums[start_index], nums[i-1]))
                start_index = i
                if i == len(nums)-1: # 순회가 끝나면
                    ranges.append(rangesToString(nums[start_index], nums[i]))
        return(ranges)

def rangesToString(a: int, b: int) -> str:
    if a == b:
        return(f"{a}")
    else:
        return(f"{a}->{b}")
                    
        
