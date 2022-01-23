from sortedcontainers import SortedList
class StockPrice(object):
    """
    Runtime: 940 ms, faster than 79.58% of Python online submissions for Stock Price Fluctuation .
    Memory Usage: 55.4 MB, less than 86.62% of Python online submissions for Stock Price Fluctuation .
    https://www.youtube.com/watch?v=iJqGjXpqdYo
    SortedList TreeMap
    
    """

    def __init__(self):
        self.prices = {}
        # sort max,min
        self.sl = SortedList()
        # last price
        self.curr = (None,None)
        

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        if timestamp in self.prices:
            self.sl.remove(self.prices[timestamp])
        if timestamp>=self.curr[0]:
            self.curr = (timestamp,price)
        
        self.sl.add(price)
        self.prices[timestamp] = price
        

    def current(self):
        """
        :rtype: int
        """
        return self.curr[1]
        

    def maximum(self):
        """
        :rtype: int
        """
        return self.sl[-1]

        

    def minimum(self):
        """
        :rtype: int
        """
        return self.sl[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()