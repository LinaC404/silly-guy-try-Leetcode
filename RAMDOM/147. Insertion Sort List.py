# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None) or (head.next is None):
            return head

        root = ListNode()
        root.next = head

        while head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                temp = head.next
                head.next = head.next.next
                q = root
                while q.next and q.next.val < temp.val:
                    q = q.next
                temp.next = q.next
                q.next = temp
        return root.next


if __name__ == "__main__":

    head = ListNode(4,ListNode(2,ListNode(1,ListNode(3))))
    ss = Solution()
    ss.insertionSortList(head)


