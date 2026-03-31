class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        capacity = 2 * n
        arr = [0] * capacity
        for i in range(n):
            arr[i] = nums[i]
            arr[i + n] = nums[i]
        return arr