# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None

        odd = head
        even = head.next
        second = head.next
        while even and even.next:
            odd.next = even.next
            odd =  odd.next
            even.next = odd.next
            even = even.next
        odd.next = second

        return head

        
        

        
if __name__=="__main__":
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    a = Solution()
    a.oddEvenList(head)