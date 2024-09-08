# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        counter = 0
        temp = head
        while temp:
            counter += 1
            temp = temp.next

        div = counter // k
        mod = counter % k

        array = []
        temp = head
        for i in range(k):
            tempDiv = div
            if mod > 0:
                tempDiv = div + 1
                mod -= 1
            head = temp
            count = 1
            while count < tempDiv and temp:
                temp = temp.next
                count += 1
            if temp:
                parent = temp
                temp = temp.next
                parent.next = None
            
            array.append(head)
        return array
        