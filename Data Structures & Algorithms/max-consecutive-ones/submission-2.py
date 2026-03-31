class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tmp = 0
        maxCon = 0
        for i in nums:
            if i == 1:
                tmp += 1
                maxCon = max(tmp, maxCon)
            else:
                tmp = 0
        return maxCon