class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            totalTime = 0
            m = l + ((r - l) // 2)
            for i in piles:
                totalTime += ((i + m - 1) // m)
            
            if totalTime <= h:
                r = m - 1
                res = m
            else:
                l = m + 1
        return res