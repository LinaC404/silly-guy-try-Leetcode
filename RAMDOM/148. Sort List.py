# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None) or (head.next is None):
            return head

        p = head
        res = []

        while p:
            res.append(p.val)
            p = p.next
        temp = head
        res.sort()
        for i in range(0,len(res)):
            temp.val = res[i]

        return head
  
                




    

if __name__ == "__main__":

    head = ListNode(4,ListNode(2,ListNode(1,ListNode(3))))
    ss = Solution()
    ss.sortList(head)
        