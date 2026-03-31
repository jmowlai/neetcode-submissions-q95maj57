class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        n = len(arr)
        for i in range(n - 1, -1, -1):
            tmp = arr[i]
            arr[i] = rightMax
            rightMax = max(rightMax, tmp)
        return arr 

