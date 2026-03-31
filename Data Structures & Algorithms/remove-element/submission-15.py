class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        cnt = 0
        for i in nums:
            if i != val:
                tmp.append(i)
                cnt += 1
        nums[:] = tmp
        return cnt 