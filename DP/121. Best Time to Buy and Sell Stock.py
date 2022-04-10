class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Runtime: 1467 ms, faster than 12.41% of Python online submissions for Best Time to Buy and Sell Stock.
        Memory Usage: 22.1 MB, less than 99.00% of Python online submissions for Best Time to Buy and Sell Stock.
        """
        res = 0
        mi = ma = prices[0]
        for i in range(1,len(prices)):
            ma = max(ma,prices[i])
            if prices[i]<mi:
                mi = prices[i]
                ma = 0
                continue
            res = max(res,ma-mi)
        return res
if __name__=="__main__":
    a = Solution()
    print(a.maxProfit([7,6,4,3,1]))




        