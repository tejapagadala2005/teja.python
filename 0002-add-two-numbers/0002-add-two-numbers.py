# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()   # dummy node to simplify result list construction
        curr = dummy
        carry = 0

        # loop until both lists are exhausted and no carry remains
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10     # compute new carry
            curr.next = ListNode(total % 10)  # create new node with digit
            curr = curr.next

            # move to the next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
