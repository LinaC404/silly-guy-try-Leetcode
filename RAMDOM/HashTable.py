key = 10

class Node (object):
    def __init__(self,data):
        self.node = data
        self.next_node = None
    
    def set_next(self,node):
        self.next_node = node
    
    def get_next(self):
        return self.next_node
    
    def get_data(self):
        return self.node
    
    def data_equals (self,data):
        return self.node == data

class HashTable(object):
    def __init__(self):
        self.val = [None] * key
    
    def search(self,data):
        i = data%key
        if self.val[i] is None:
            return None
        else:   
            head = self.val[i]
            while head and not head.data_equals(data):
                head = head.get_next()
            if head:
                return head
            else:
                return False

    def insert(self,data):
        if self.search(data):
            return True
        i = data%key
        node = Node(data)
        if self.val[i] is None:
            self.val[i] = node
            return True
        else:
            head = self.val[i]
            while head.get_next() is not None: 
                head =  head.get_next()
            head.set_next(node)
            return True 

    def delete(self,data):
        if self.search(data):
            i = data%key
            if self.val[i].data_equals(data):
                self.val[i] = self.val[i].get_next()
            else:
                head = self.val[i]
                while not head.get_next().data_equals(data):
                    head = head.get_next()
                head.set_next(head.get_next().get_next())
                return True

        else:
            return False
    
    def echo(self):
        i = 0
        for head in self.val:
            print(str(i)+':\t')
            if head is None:
                print ('None')
            else:
                while head is not None:
                    print(str(head.get_data())+'->',)
                    head = head.get_next()
                print('None')
            print(' ')

            i = i+1
        print(' ')

if __name__ == '__main__':
    hashset = HashTable()
    hashset.insert(10)
    hashset.insert(11)
    hashset.insert(1)
    hashset.echo()
    hashset.delete(1)
    hashset.echo()
