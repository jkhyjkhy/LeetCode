class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_enumerate = [(num, i) for i, num in enumerate(nums)]
        nums_enumerate.sort(key=lambda x: x[0]) # 키값을 람다로 가져가는것 반드시 기억

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums_enumerate[left][0] + nums_enumerate[right][0] < target:
                left += 1
            elif nums_enumerate[left][0] + nums_enumerate[right][0] > target:
                right -= 1
            else:
                return([nums_enumerate[left][1],nums_enumerate[right][1]])