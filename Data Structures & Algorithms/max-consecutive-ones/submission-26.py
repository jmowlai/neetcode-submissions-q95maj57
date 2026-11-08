class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = count = 0
        for x in nums:
            count = count + 1 if x else 0
            best = max(best, count)
        return best