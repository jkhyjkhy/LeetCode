from collections import Counter
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        # dog, cat, cat, dog
        
        counter_pattern = {}
        counter_word = {}
        
        if len(s) != len(pattern):
            return False
        
        for i in range(len(s)):
            if pattern[i] in counter_pattern:
                if counter_pattern[pattern[i]] != s[i]:
                    return False
            else:
                counter_pattern[pattern[i]] = s[i]
            if s[i] in counter_word:
                if counter_word[s[i]] != pattern[i]:
                    return False
            else:
                counter_word[s[i]] = pattern[i]
        return True
                