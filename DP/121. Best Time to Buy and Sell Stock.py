class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Runtime: 1867 ms, faster than 5.03% of Python online submissions for Best Time to Buy and Sell Stock.
        Memory Usage: 22.5 MB, less than 76.79% of Python online submissions for Best Time to Buy and Sell Stock.
        """
        ans = 0
        stock = [prices[0]]
        for i in range(1,len(prices)):
            if stock: ans = max(ans,stock[-1]-stock[0])
            if prices[i]>stock[-1]:
                stock.append(prices[i])
                continue
            while stock and stock[-1]>=prices[i]:
                stock.pop()
            stock.append(prices[i])
        return max(ans,stock[-1]-stock[0])

    def maxProfit(self, prices):
        """
        Runtime: 1280 ms, faster than 33.89% of Python online submissions for Best Time to Buy and Sell Stock.
        Memory Usage: 22.7 MB, less than 56.56% of Python online submissions for Best Time to Buy and Sell Stock.
        """
        # min -> monotone decreasing
        # max -> monotone increasing
        ans = 0
        min_p = 10001
        max_p = -1
        for p in prices:
            if p<min_p:
                # no update, the price is decreasing
                # the max_p should be initialized to avoid [...,max,...,min,...]
                min_p = p
                max_p = -1
            elif p>max_p:
                max_p = p
                ans = max(ans,max_p-min_p)
        return ans

        
if __name__ == "__main__":
    prices =  [2,1,2,1,0,1,2]
    a = Solution()
    print(a.maxProfit(prices))