class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            if len(nums) <= 2:
                return len(nums)

            index = 2  # 중복을 최대 두 번까지만 허용하는 경우
            for i in range(2, len(nums)):
                if nums[i] != nums[index - 2]:
                    nums[index] = nums[i]
                    index += 1

            return index