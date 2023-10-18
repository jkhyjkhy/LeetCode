# import math
class Solution:
    def isHappy(self, n: int) -> bool:
        # 파이참에서 구동해본 결과 해피넘버가 아니면 영원히 순환함
        seen_n = set() # 순환이 안되게 집합(set) 사용
        while n != 1:
            if n in seen_n:
                return False
            seen_n.add(n)
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n //= 10
            n = total
        return True
    
    
    
# 해보다 안돼서 그냥 덮어버린 코드, False 처리가 어려움 
# -> 더 간단하게 1의 자리에서부터 확인하면 쉽게 풀림    
#         total = 0
#         current_tap = 0
#         if(int(math.log10(n)) == 0):
#             return False
#         while n != 1:
#             digit = int(math.log10(n))
#             while digit > 0:
#                 current_tap = (n//(10 ** digit))
#                 total += (current_tap ** 2)
#                 n -= current_tap * (10 ** digit)
#                 digit -= 1
#             n = total
        
#         return True
