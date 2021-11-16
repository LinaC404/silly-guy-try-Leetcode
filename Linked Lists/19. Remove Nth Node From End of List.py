# Definition for singly-linked list.
from collections import defaultdict
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MySolution(object):
    def removeNthFromEnd(self, head, n):
        """
        Runtime: 24 ms
        Memory Usage: 13.5 MB
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        index = 0
        node_dict = defaultdict()
        while p:
            node_dict[index] = p
            p = p.next
            index = index + 1
        print(node_dict)

        total = index - 1
        if n == total: return head.next

        remove = total-n+1
        print(remove)
        ppre = node_dict[remove-1]
        pnext = node_dict[remove].next
        ppre.next = pnext
        return start

"""快慢指针
e.g.
n = 2
dummy->1 ->2 -> 3 ->4 ->5
  f
       f
  s        f
       s        f
           s         f
                s        f
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        for i in range(n):
            fast = fast.next
        # 取fast.next, 因为想得到被删除元素前一元素
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
        

         


        

head = ListNode(1,(ListNode(2,ListNode(3,ListNode(4,ListNode(5))))))
n = 5
a = Solution()
a.removeNthFromEnd(head,n)
        