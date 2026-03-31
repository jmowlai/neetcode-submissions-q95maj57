class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m] + nums2[:n]
        self.mergeSortHelper(nums1, 0, len(nums1) - 1)

    def mergeSortHelper(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        m = (s + e) // 2
        self.mergeSortHelper(arr, s, m)
        self.mergeSortHelper(arr, m + 1, e)
        self.mergeArr(arr, s, m, e)
        return arr
    
    def mergeArr(self, arr, s, m, e):
        L = arr[s:m + 1]
        R = arr[m + 1: e + 1]

        i = j = 0
        k = s

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1  
