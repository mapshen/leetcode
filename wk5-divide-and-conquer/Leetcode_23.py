# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge2(list1,list2):
            head=root=ListNode(0)
            while list1 and list2:
                if list1.val<=list2.val:
                    head.next= list1
                    head=list1
                    list1=list1.next
                else:
                    head.next=list2
                    head=list2
                    list2=list2.next
            if list1:
                head.next = list1
                return root.next
            if list2:
                head.next = list2
                return root.next
            return root.next
      
        if len(lists) == 0:
            return
        
        n = len(lists)
        interval = 1
        while interval<n:
            for i in range(0,n-interval,interval*2):
                lists[i]=merge2(lists[i],lists[i+interval])
            interval*=2
          
        return lists[0] if n>0 else lists
