class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tmp = -1
        for i in range(len(arr) - 1, -1, -1):
            tmp, arr[i] = max(arr[i], tmp), tmp
        return arr