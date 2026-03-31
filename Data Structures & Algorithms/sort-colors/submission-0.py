class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0] * 3
        for n in nums:
            cnt[n] += 1

        i = 0
        for n in range(len(cnt)):
            for _ in range(cnt[n]):
                nums[i] = n
                i += 1
        
        return nums