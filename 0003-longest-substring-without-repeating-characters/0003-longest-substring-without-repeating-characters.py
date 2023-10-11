class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = []
        counter = 0
        start = 0
        for i in range(len(s)):
            while s[i] in index:
                index.pop(0)
                start += 1
            index.append(s[i])
            counter = max(counter, i-start+1)
        
        return(counter)