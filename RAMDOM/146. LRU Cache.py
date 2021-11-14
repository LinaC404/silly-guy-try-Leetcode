class ListNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = self 
        self.next = self

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = dict()
        self.capacity = capacity
        self.size = 0
        self.root = ListNode(0,0)
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            node = self.dict[key]
            self.RemoveL(node)
            self.insertH(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            node = self.dict[key]
            self.RemoveL(node)
            self.insertH(node)
            node.value = value   
        else:
            if self.size == self.capacity:
                self.RemoveT()
                self.size = self.size - 1
            node = ListNode(key,value)
            self.insertH(node)
            self.dict[key] = node
            self.size = self.size + 1

    def RemoveL(self,node):
        if node == self.root:
            return
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node 
        node.prev  = node.next = None

    def insertH(self,node):
        head_node = self.root.next
        head_node.prev = node
        node.prev = self.root
        self.root.next = node
        node.next = head_node
    
    def RemoveT(self):
        if self.size == 0:
            return
        tail_node = self.root.prev
        del self.dict[tail_node.key]
        self.RemoveL(tail_node)


# Your LRUCache object will be instantiated and called as such:
if __name__ == '__main__':
    obj = LRUCache(2)
    # obj.put(1,1)
    # obj.put(2,2)
    # param_1 = obj.get(1)
    # obj.put(3,3)
    # param_2 = obj.get(2)
    # obj.put(4,4)
    # param_3 = obj.get(1)
    # param_4 = obj.get(3)
    # param_5 = obj.get(4)
    