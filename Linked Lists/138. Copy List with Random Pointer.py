# Definition for a Node.

from collections import defaultdict
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution(object):
    def copyRandomList(self, head):
        """ HINT:
            Old List: A --> B --> C --> D
            InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'
        :type head: Node
        :rtype: Node
        """
        if not head: return None
        p1 = head
        # copy the same next
        while p1:
            copy = Node(p1.val,p1.next,p1.random)
            copy.next = p1.next
            p1.next = copy
            p1 = copy.next

        # copy the random
        p2 = head
        while p2:
            p2.next.random = None if p2.random is None else p2.random.next
            p2 = p2.next.next

        res = head.next
        p3 = head
        # remove the orininal
        while p3:
            node = p3.next
            p3.next = node.next
            node.next = None if node.next is None else node.next.next
            p3 = p3.next
        return res

            
