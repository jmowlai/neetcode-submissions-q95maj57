# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        parent = None
        curr = root

        while curr and curr.val != key:
            parent = curr
            if key > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        
        if not curr:
            return root
        
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right
            if not parent:
                return child
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child
        else:
            par = None
            delNode = curr
            curr = curr.left
            while curr.right:
                par = curr
                curr = curr.right
            
            if par:
                par.right = curr.left
                curr.left = delNode.left
            
            curr.right = delNode.right

            if not parent:
                return curr
            
            if parent.right == delNode:
                parent.right = curr
            else:
                parent.left = curr
            
        
        return root

