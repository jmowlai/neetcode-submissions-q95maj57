class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        k = 0
        for i in nums:
            if i != val:
                tmp.append(i)
                k += 1
        nums[:] = tmp
        return k