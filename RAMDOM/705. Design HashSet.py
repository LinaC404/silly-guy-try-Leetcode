# class Node(object):
#     def __init__(self, data, next_node=None):
#         self.data = data
#         self.next_node = next_node
    
#     def set_next(self, node):
#         self.next_node = node

#     def get_next(self):
#         return self.next_node
    
#     def get_data(self):
#         return self.data

#     def data_equals (self,data):
#         return self.data == data


# class MyHashSet(object):

#     def __init__(self):
#         self.val = [None] * 10
#         self.flag = 10
        

#     def add(self, key):
#         """
#         :type key: int
#         :rtype: None
#         """
#         i = key%self.flag
#         node = Node(key)
#         if self.val[i] is None:
#             self.val[i] = node
#             return None
#         else:
#             head = self.val[i]
#             while head.get_next() is not None:
#                 head = head.get_next()
#             head.set_next(node)
#             return None
            

#     def remove(self, key):
#         """
#         :type key: int
#         :rtype: None
#         """
#         print(self.contains(key))
#         if self.contains(key) is False:
#             return None

#         i = key%self.flag
#         head = self.val[i]
#         if head.get_data() == key:
#             self.val[i] = head.get_next()
#             if self.contains(key) is True:
#                 self.remove(key)
#             return None
#         else:
#             head = self.val[i]
#             while head.get_next().get_next() is not None and head.get_next().get_data() is not key:
#                 head = head.get_next()
#             head.set_next(head.get_next().get_next())
#             if self.contains(key) is True:
#                 self.remove(key)
#         return None

#     def contains(self, key):
#         """
#         Returns true if this set contains the specified element
#         :type key: int
#         :rtype: bool
#         """

#         i = key%self.flag
#         if self.val[i] is None:
#             return False
#         else:   
#             head = self.val[i]
#             while head.get_next() is not None and not head.data_equals(key):
#                 head = head.get_next()
#             if head:
#                 return True
#             else:
#                 return False


#     def echo(self):
#         i = 0
#         for head in self.val:
#             print(str(i)+':\t')
#             if head is None:
#                 print ('None')
#             else:
#                 while head is not None:
#                     print(str(head.get_data())+'->',)
#                     head = head.get_next()
#                 print('None')
#             print(' ')

#             i = i+1
#         print(' ')

        
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data=[-1]*1000001
        
    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.data[key]==-1:
            self.data[key]=1
       
    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.data[key]=-1
      
    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.data[key]==1

# Your MyHashSet object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    obj.add(2)
    obj.add(2)
    obj.add(2)

    obj.remove(2)

    print(obj.contains(2))
