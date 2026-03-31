class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} # Initialise hashmap value: count
        freq = [[] for i in range(len(nums) + 1)] # Array of input length

        for i in nums: # for each number
            count[i] = 1 + count.get(i, 0) # Increment count of said number by 1
        for i, j in count.items(): # For each value:count pair
            freq[j].append(i) #Add the value to the associated freq list
        
        res = []
        for i in range(len(freq) - 1, 0, -1): # Working backwards in the list
            for j in freq[i]: # For each element in the freq sub-array
                res.append(j) # Append the value
                if len(res) == k: # If same size as k then return result
                    return res