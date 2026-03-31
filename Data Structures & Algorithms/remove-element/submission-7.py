class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        for i in nums:
            if i != val:
                tmp.append(i)
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)
        