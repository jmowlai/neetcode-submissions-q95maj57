class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i, j = 0, len(heights) - 1

        while i < j:
            curAmt = (j - i) * min(heights[i], heights[j])
            res = max(res, curAmt)
            if heights[i] <= heights[j]:
                i += 1
                # res = max(res, curAmt)
            elif heights[j] < heights[i]:
                j -= 1
                # res=max(res, curAmt)
        
        return res
            