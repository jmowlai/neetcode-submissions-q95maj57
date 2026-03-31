# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        currn = list1
        currm = list2
        arr = []
        while currn:
            arr.append(currn.val)
            currn = currn.next
        while currm:
            arr.append(currm.val)
            currm = currm.next
        
        arr.sort()
        dummy = node = ListNode()

        for i in arr:
            node.next = ListNode(i)
            node = node.next 
        
        return dummy.next
