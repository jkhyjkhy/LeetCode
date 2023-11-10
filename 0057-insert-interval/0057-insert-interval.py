class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        
        if not intervals:
            return intervals
        
        current_interval = intervals[0]
        list_interval = []
        for interval in intervals[1:]:
            if current_interval[1] >= interval[0]:
                current_interval[1] = max(interval[1], current_interval[1])
            else:
                list_interval.append(current_interval)
                current_interval = interval
        list_interval.append(current_interval)
        
        return list_interval