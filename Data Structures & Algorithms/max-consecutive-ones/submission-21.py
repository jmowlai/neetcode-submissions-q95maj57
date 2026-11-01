class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = count = 0
        for i in nums:
            if i == 1:
                count += 1
                best = max(best, count)
            else:
                count = 0
        
        return best