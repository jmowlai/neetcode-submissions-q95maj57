class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # Hashmap to contain values that have been checked

        for i, j in enumerate(nums): # Creates an index for each element
            diff = target - j # Get the associated number to satisfy criteria
            if diff in prevMap: # If associated number exists in previous has
                return [prevMap[diff], i] # Return index of the value of the associated number and the current
            prevMap[j] = i # Otherwise add the current value and its index to the hashmap
