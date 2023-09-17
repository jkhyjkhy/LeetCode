class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        starting_spot = 0
        current_gas = 0
        total_gas = 0
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            total_gas += gas[i] - cost[i]
            
            if current_gas < 0:
                current_gas = 0
                starting_spot = i+1
            
        if total_gas < 0:
            return -1
        else:
            return starting_spot



# 시간 초과로 인해 실패하고 다음에 고쳐볼 코드

#         if len(gas) == 1 and gas[0] >= cost[0]:
#             return 0
        
#         able_starting_point = [i for i in range(len(gas)) if gas[i] - cost[i] >= 0] # 리스트 컴프리헨션으로 가능한 시작지점을 찾음
#         if not able_starting_point:  # 가능한 시작 지점이 없는 경우
#             return -1
        
        
#         for starting_spot in able_starting_point:
#             current_gas = 0
#             current_spot = starting_spot
#             for n in range(len(gas)):
#                 current_gas += gas[current_spot] # 현 시점에서 가스를 먼저 채우고
#                 current_gas -= cost[current_spot] # 현 지점에서 다음 지점으로 이동하는데에 드는 코스트를 계산
#                 if current_gas < 0:
#                     break
#                 current_spot = (current_spot+1) % len(gas)
#             if current_gas >= 0:
#                 return starting_spot
            
#         return -1