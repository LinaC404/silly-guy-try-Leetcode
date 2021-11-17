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
        curr = head
        while curr:
            curr_next = curr.next
            copy_curr = Node(curr.val,curr_next,curr.random)
            curr.next = copy_curr
            copy_curr.next = curr_next
            curr = curr_next
            print(copy_curr)

        # while p2:
        #     print(p2.val)
        #     print(p2.next)
        #     p2 = p2.next
        p2 = head.next
        res = head.next
        print(p2.val)
        print("Next",p2.next)
        print("Random",p2.random)
        while p2.next:
            the_next = p2.next.next
            the_random = None if p2.random is None else p2.random.next
            p2.next = the_next
            p2.random = the_random
            p2 = the_next
            print(p2.val)
            print("Next",p2.next)
            print("Random",p2.random.val)
        return res
            

        
if __name__=="__main__":
    head = Node(7,Node(13,Node(11,Node(10,Node(1)))))
    point_dict = defaultdict()
    p = head
    while p:
        point_dict[p.val] = p
        p = p.next
    print(point_dict)
    point_dict[7].random = None
    point_dict[13].random = point_dict[7]
    point_dict[11].random = point_dict[1]
    point_dict[10].random = point_dict[11]
    point_dict[1].random = point_dict[7]
    a = Solution()
    a.copyRandomList(head)