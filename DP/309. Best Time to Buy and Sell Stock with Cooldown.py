class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        https://www.youtube.com/watch?v=oL6mRyTn56M
        Runtime: 33 ms, faster than 69.95% of Python online submissions for Best Time to Buy and Sell Stock with Cooldown.
        Memory Usage: 13.6 MB, less than 83.61% of Python online submissions for Best Time to Buy and Sell Stock with Cooldown.
        """
        # (keep:hold[i-1],buy:rest[i-1]-price[i]) -> current holding profits
        hold = float("-inf")
        # (sell:hold[i-1]+price[i]) -> sell the stock
        sell = 0
        # (keep:rest[i-1],sell[i-1]) -> cooldown state
        rest = 0

        for i in range(len(prices)):
            temp = rest
            rest = max(rest,sell)
            sell = hold + prices[i]
            hold = max(hold,temp-prices[i])
        return max(sell,rest)
     
if __name__=="__main__":
    a = Solution()                 
    print(a.maxProfit(prices = [1,2,3,0,2]))