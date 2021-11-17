# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MySolution(object):
    def mergeTwoLists(self, l1, l2):
        """
        Runtime: 24 ms
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None: return None
        if l1 is None: return l2
        if l2 is None: return l1
        p1,p2 = l1,l2
        dummy = ListNode(0)
        start = dummy
        while p1 or p2:
            if p1 is None:
                dummy.next = p2
                break
            if p2 is None:
                dummy.next = p1
                break

            if p1.val<=p2.val:
                dummy.next=ListNode(p1.val)
                dummy = dummy.next
                p1 = p1.next
            else:
                dummy.next=ListNode(p2.val)
                dummy = dummy.next
                p2 = p2.next
        return start.next
        
    
if __name__=="__main__":
    # l1 = ListNode(1,ListNode(2,ListNode(4,ListNode(5))))
    # l2 = ListNode(1,ListNode(3))
    l1 = ListNode()
    l2 = ListNode()
    a = MySolution()
    a.mergeTwoLists(l1,l2)