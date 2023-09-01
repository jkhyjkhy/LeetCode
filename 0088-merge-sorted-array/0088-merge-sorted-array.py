class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for x in range(m, m+n):
            nums1[x]=nums2[x-m]
        nums1.sort()

        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        