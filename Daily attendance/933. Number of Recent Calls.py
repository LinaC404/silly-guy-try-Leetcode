class RecentCounter(object):
    """
    Runtime: 413 ms, faster than 41.23% of Python online submissions for Number of Recent Calls.
    Memory Usage: 18.9 MB, less than 5.26% of Python online submissions for Number of Recent Calls.
    """

    def __init__(self):
        self.l = 0
        self.toatl = 0
        self.req = []

        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.req.append(t)
        self.toatl += 1

        while self.req[self.l]<t-3000:
            self.l += 1
            self.toatl -= 1
        return self.toatl



        


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
obj.ping(1)
obj.ping(100)
obj.ping(3001)
obj.ping(3002)
