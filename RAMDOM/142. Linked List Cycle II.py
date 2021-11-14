# 关于快慢指针确定是否拥有闭环
# 设一指针回到起点，两指针均指向the next ,相遇处即为交点
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        
        fast = head
        slow = head
        mark = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while mark != slow:
                    mark = mark.next
                    slow = slow.next
                return mark
        return None
                
                
            
        
        
