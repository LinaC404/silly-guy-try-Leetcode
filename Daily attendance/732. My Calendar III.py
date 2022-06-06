import bisect
class MyCalendarThree:
    """
    Runtime: 2167 ms, faster than 33.78% of Python3 online submissions for My Calendar III.
    Memory Usage: 14.3 MB, less than 60.32% of Python3 online submissions for My Calendar III.
    """
    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> int:
        l_index = bisect.bisect_left(self.arr, [start, 1])
        r_index = bisect.bisect_right(self.arr, [end, -1])
        self.arr.insert(l_index, [start, 1])
        self.arr.insert(r_index+1, [end, -1])
        res = 0
        cur = 0
        for i in range(len(self.arr)):
            cur += self.arr[i][1]
            res = max(res,cur)
        return res



# Your MyCalendarThree object will be instantiated and called as such:
if __name__=="__main__":
    obj = MyCalendarThree()
    print("--",obj.book(10,20))
    print("--",obj.book(50,60))
    print("--",obj.book(10,40))
    print("--",obj.book(5,15))
    print("--",obj.book(5,10))
    print("--",obj.book(25,55))
    