class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxCnt = 0
        for i in nums:
            if i:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 0
        return maxCnt
