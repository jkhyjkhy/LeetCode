class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        jumps = 0  # 점프 횟수를 초기화
        current_position = 0  # 현재 위치를 초기화

        while current_position < n - 1:
            max_jump = 0  # 현재 위치에서 가능한 최대 점프 거리 초기화
            next_position = current_position  # 다음 위치를 현재 위치로 초기화

            # 현재 위치에서 가능한 점프 거리 중 가장 먼 위치를 찾음
            for j in range(1, nums[current_position] + 1):
                if current_position + j >= n - 1:
                    return jumps + 1  # 마지막 위치에 도달하면 점프 횟수 반환
                if current_position + j + nums[current_position + j] > next_position + max_jump:
                    next_position = current_position + j
                    max_jump = nums[current_position + j]

            current_position = next_position  # 다음 위치로 이동
            jumps += 1  # 점프 횟수 증가

        return jumps


            
            