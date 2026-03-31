class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # Hashmap to contain values that have been checked

        for i, j in enumerate(nums):
            diff = target - j
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[j] = i
