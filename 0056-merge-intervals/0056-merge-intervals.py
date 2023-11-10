class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        if not intervals:
            return intervals
        current_range = intervals[0]
        ranges = []
        
        for interval in intervals[1:]:
            if current_range[1] >= interval[0]:
                current_range[1] = max(current_range[1],interval[1]) # 범위가 일부만 겹치는것도 고려해야함 max 이용
            else:
                ranges.append(current_range)
                current_range = interval
        
        ranges.append(current_range)
        
        return ranges