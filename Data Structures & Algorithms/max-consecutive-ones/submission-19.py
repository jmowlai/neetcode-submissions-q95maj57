class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        res = 0
        for i in range(n):
            cnt += 1 if nums[i] else -cnt
            res = max(res, cnt)
        return res
