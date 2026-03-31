class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = nums1[:m]
        i = j = idx = 0
        while idx < m + n:
            if j >= n or (i < m and tmp[i] <= nums2[j]):
                nums1[idx] = tmp[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1
            idx += 1    
        