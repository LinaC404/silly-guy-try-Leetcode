class OrderedStream:

    def __init__(self, n: int):
        self.chunks = [0]*n
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.chunks[idKey-1] = value
        print(self.chunks)
        ans = []
        for i in range(idKey-1,self.n):
            if self.chunks[i]==0:
                return ans
            else:
                ans.append(self.chunks[i])
        return ans
            
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)