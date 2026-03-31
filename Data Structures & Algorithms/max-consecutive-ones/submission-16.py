class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxCnt = 0
        for i in range(len(nums)):
            cnt += 1 if nums[i] else -cnt
            maxCnt = max(cnt, maxCnt)
        return maxCnt  