from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = len(t)
        counter = Counter(t)
        window = ""
        left = 0
        min_window=max_window = 0

        for right in range(len(s)):
            count -= counter[s[right]] > 0
            counter[s[right]] -= 1
            if count == 0:
                while left < right and counter[s[left]] < 0:
                    counter[s[left]] += 1
                    left += 1
                if not max_window or right - left <= max_window - min_window:
                    max_window, min_window = right, left
                    window = s[min_window:max_window+1]
                    count += 1
                    counter[s[left]] += 1
                    left += 1
                    
        return window