class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = j = 0
        i = -1

        while j < n:
            if nums[j] != 0:
                j += 1
                continue
            
            cnt = max(cnt, j - i - 1)
            i = j 
            j += 1
        
        cnt = max(cnt, j - i - 1)
        return cnt

        