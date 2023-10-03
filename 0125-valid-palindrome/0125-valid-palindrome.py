class Solution:
    def isPalindrome(self, s: str) -> bool:
        par = ''.join(filter(str.isalnum, s)).lower()
        if(len(par) == 0):
            return True
        start = 0
        end = len(par)-1
        
        while start < end:
            if par[start] != par[end]:
                return False
            start += 1
            end -= 1
        
        return True
            