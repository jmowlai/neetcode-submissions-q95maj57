class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        maxRight = -1
        for i in range(n - 1, -1, -1):
            res[i] = maxRight
            maxRight =  max(arr[i], maxRight)
        return res 