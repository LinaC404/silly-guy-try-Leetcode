from functools import cache
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        Runtime: 1053 ms, faster than 50.69% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
        Memory Usage: 184.2 MB, less than 13.36% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
        """
        @cache
        def dp(i):
            #  return tuple (sold:max profit of holing stock(we can sell),holding: max profit of not holding(we can buy))
            if i < 0: return 0,float("-inf")
            sold,holding = dp(i-1)
            return(max(sold,holding+prices[i]-fee),max(holding,sold-prices[i]))
        return dp(len(prices)-1)[0]




if __name__=="__main__":
    prices = [1,3,2,8,4,9]
    fee = 2
    a = Solution()
    print(a.maxProfit(prices,fee))
        