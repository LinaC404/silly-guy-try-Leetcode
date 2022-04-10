class Solution(object):
    def mymaxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Runtime: 105 ms, faster than 28.46% of Python3 online submissions for Best Time to Buy and Sell Stock II.
        Memory Usage: 15.1 MB, less than 72.19% of Python3 online submissions for Best Time to Buy and Sell Stock II.
        """
        res = 0
        queue = [prices[0]]
        for i in range(1,len(prices)):
            if queue and prices[i]<queue[-1]:
                res += queue[-1]-queue[0]
                queue = []
            queue.append(prices[i])
        res += queue[-1]-queue[0]
        return res
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Runtime: 56 ms, faster than 98.53% of Python3 online submissions for Best Time to Buy and Sell Stock II.
        Memory Usage: 15.1 MB, less than 97.97% of Python3 online submissions for Best Time to Buy and Sell Stock II.
        """
        res = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                res += prices[i+1] - prices[i]
        return res


if __name__=="__main__":
    prices = [1,2,3,4,5]
    a = Solution()
    print(a.maxProfit(prices))