class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        for i in range(n):
            maxVal = -1
            for j in range(i + 1, n):
                maxVal = max(maxVal, arr[j])
            res.append(maxVal)
        return res 

