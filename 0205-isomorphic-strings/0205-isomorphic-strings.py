from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        isomorphic_s = {}
        isomorphic_t = {}
        
        for i in range(len(s)):
            if s[i] in isomorphic_s:
                if isomorphic_s[s[i]] != t[i]:
                    return False
            else:
                isomorphic_s[s[i]] = t[i]

            if t[i] in isomorphic_t:
                if isomorphic_t[t[i]] != s[i]:
                    return False
            else:
                isomorphic_t[t[i]] = s[i]
                
        return True