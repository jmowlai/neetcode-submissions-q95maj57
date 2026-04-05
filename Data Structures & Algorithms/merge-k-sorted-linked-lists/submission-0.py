# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        for i in range(1, len(lists)):
            lists[i] = self.merge(lists[i - 1], lists[i])

        return lists[-1]

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = ListNode()
        self.tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                self.tail.next = l1
                l1 = l1.next
            else:
                self.tail.next = l2
                l2 = l2.next
            self.tail = self.tail.next
        if l1:
            self.tail.next = l1
        if l2:
            self.tail.next = l2

        return dummy.next