import random
"""
Runtime: 1538 ms, faster than 18.18% of Python online submissions for Design Skiplist.
Memory Usage: 27.2 MB, less than 9.09% of Python online submissions for Design Skiplist.
"""
class Node:
    def __init__(self,val=-1,right=None,down=None):
        self.val = val
        self.right = right
        self.down = down

class Skiplist(object):

    def __init__(self):
        # start with a dummy head
        self.head = Node()
        

    def search(self, target):
        """
        :type target: int
        :rtype: bool
        """
        # it has many levels
        node = self.head
        while node:
            # find the previous node of target
            while node.right and node.right.val < target:
                node = node.right
            if node.right and node.right.val == target:
                return True
            # do not forget to move to the next level
            node = node.down
        return False
        

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        # store all the previous nodes
        pre_nodes_list = []
        node = self.head
        while node:
            while node.right and node.right.val < num:
                node = node.right
            # Not node.right here, what we need id the pre node
            pre_nodes_list.append(node)
            node = node.down
        
        # insert the node from bottom to up
        # !Create a new level if the probability 
        # Mark the new trick...
        insert = True
        down = None
        # the condition here should include `insert`
        while insert and pre_nodes_list:
            pre = pre_nodes_list.pop()
            pre.right = Node(num,pre.right,down)
            down = pre.right
            insert = (random.getrandbits(1)==0)
        
        if insert:
            self.head = Node(-1,None,self.head)

    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        node = self.head
        mark = False
        while node:
            while node.right and node.right.val < num:
                node = node.right
            if node.right and node.right.val == num:
                node.right = node.right.right
                mark = True
            node = node.down
        return mark


# Your Skiplist object will be instantiated and called as such:
if __name__=="__main__":
    a = Skiplist()
    print(a.add(1))
    print(a.add(2))
    print(a.add(3))
    print(a.search(0))
    print(a.add(4))
    print(a.search(1))
    print(a.erase(0))
    print(a.erase(1))
    print(a.search(1))

# https://www.youtube.com/watch?v=783qX31AN08
