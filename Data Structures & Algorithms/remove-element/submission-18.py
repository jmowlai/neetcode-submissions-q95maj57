class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr = []
        cnt = 0
        for num in nums:
            if num != val:
                arr.append(num)
                cnt += 1
        
        nums[:] = arr
        return cnt