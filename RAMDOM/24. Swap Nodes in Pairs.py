# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution(object):
    def traverse(self,head):
        length = 0
        while not head is None:
            length = length + 1
            print(head.val)
            head = head.next   
        return length 

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return headNo
        cur = head
        head = head.next
        if not head.next is None:
            cur.next = self.swapPairs(head.next)
        else:
            cur.next = None
        head.next = cur
        return head
             


if __name__ == '__main__':
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
    # head  = ListNode(1,ListNode(2))
    a = Solution()
    result = a.swapPairs(head)
    a.traverse(head)
    a.traverse(result)