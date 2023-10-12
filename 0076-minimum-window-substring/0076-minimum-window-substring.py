# 다시 풀어볼 문제
# 내 코드가 동작하지 않아 

# StefanPochmann의 12 lines Python 해설을 참고함
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, missing = Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while need[s[i]] < 0: need[s[i]] += 1; i += 1
                if not J or j - i <= J - I: I, J = i, j
                need[s[i]] += 1; i += 1; missing += 1       # SPEEEEEEEED UP!
        return s[I : J]