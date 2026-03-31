# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        cnt = 0

        while head:
            arr.append(head.val)
            head = head.next
            cnt += 1
        
        dummy = node = ListNode()
        for i in range(cnt - 1, -1, -1):
            node.next = ListNode(arr[i])
            node = node.next
        
        return dummy.next