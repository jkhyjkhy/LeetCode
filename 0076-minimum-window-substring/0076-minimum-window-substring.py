from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        count = len(t)
        counter = Counter(t)
        left = 0
        min_len = float('inf')
        min_window = ""
        
        for right in range(len(s)):
            if counter[s[right]] > 0:
                count -= 1
            counter[s[right]] -= 1
            
            while count == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]
                
                if counter[s[left]] == 0:
                    count += 1
                counter[s[left]] += 1
                left += 1
        
        return min_window