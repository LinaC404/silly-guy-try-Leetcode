from collections import deque
class MyCircularDeque:
    """
    Runtime: 99 ms, faster than 63.03% of Python3 online submissions for Design Circular Deque.
    Memory Usage: 14.6 MB, less than 60.45% of Python3 online submissions for Design Circular Deque.
    """

    def __init__(self, k: int):
        self.s = deque([])
        self.k = k
        self.l = 0
        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.s.appendleft(value)
        self.l += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.s.append(value)
        self.l += 1
        return True
        
        
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.s.popleft()
        self.l -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.s.pop()
        self.l -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.s[0]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.s[-1]
        

    def isEmpty(self) -> bool:
        if self.l == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.l < self.k:
            return False
        return True
