# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root:
            return False
        if self.doesPathExist(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def doesPathExist(self, head: ListNode, node: TreeNode) -> bool:
        if not head:
            return True
        if not node:
            return False
        if head.val != node.val:
            return False
        return self.doesPathExist(head.next, node.left) or self.doesPathExist(head.next, node.right)    