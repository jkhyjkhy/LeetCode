class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        current_range = []
        start_index = 0
        
        if len(nums) == 1: # 배열의 요소가 하나면
            ranges.append(rangesToString(nums[0],nums[0]))
            return ranges
        
        for i in range(1, len(nums)): # 아니라면
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

def rangesToString(a: int, b: int) -> str: # 정답 양식에 맞는 전환 함수
    if a == b:
        return(f"{a}")
    else:
        return(f"{a}->{b}")
                    
        
