# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return False
        curr = head
        res = set()
        while curr:
            if curr in res:
                return True
            res.add(curr)
            curr = curr.next
        return False
        