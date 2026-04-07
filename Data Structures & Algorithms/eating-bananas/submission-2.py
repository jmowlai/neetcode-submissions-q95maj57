class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def bs(l, r, res):
            if l > r:
                return res
            
            m = l + (r - l) // 2

            totalTime = 0
            for p in piles:
                totalTime += (p + m - 1) // m
            
            if totalTime <= h:
                return bs(l, m - 1, m)
            else:
                return bs(m + 1, r, res)
            
        return bs(1, max(piles), max(piles))

