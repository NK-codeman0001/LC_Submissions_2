# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums, head):
        bs = [False] * 100001
        for num in nums:
            bs[num] = True

        dummy = ListNode(-1, head)
        prev = dummy

        while head:
            if bs[head.val]:
                prev.next = head.next
            else:
                prev = head
            head = head.next

        return dummy.next
        