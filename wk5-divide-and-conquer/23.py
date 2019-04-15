# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return []

        k = len(lists)
        while k > 1:
            n = (k + 1) // 2
            for i in range(k // 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + n])
            k = n

        return lists[0]

    def merge2Lists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        current.next = l1 if l1 else l2
        return dummy.next
