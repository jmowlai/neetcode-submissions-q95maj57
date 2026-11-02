class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = [0] * (2 * n)
        for i in range(n):
            arr[2 * i] = nums[i]
            arr[(2 * i) + 1] = nums[i + n]
        return arr
