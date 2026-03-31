class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n):
            maxVal = 0
            if i == n-1 :
                arr[i] = -1
            else:
                for j in range(i + 1, n):
                    maxVal = max(maxVal, arr[j])
                    arr[i] = maxVal

        return arr