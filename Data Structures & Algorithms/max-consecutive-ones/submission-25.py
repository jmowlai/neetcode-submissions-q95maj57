class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = count = 0
        for i in nums:
            count = count + 1 if i else 0
            best = max(best, count)
        return best