class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total = 1
        if num == total:
            return False
        
        for i in range(2, int(num**0.5)+1): # 제곱근까지만 계산
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
                
        
        return True if num == total else False