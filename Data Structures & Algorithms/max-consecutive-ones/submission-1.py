class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxVal = 0
        currVal = 0
        for i in nums:
            if i == 1:
                currVal += 1
                maxVal = max(currVal, maxVal)
            else:
                currVal = 0
        return maxVal