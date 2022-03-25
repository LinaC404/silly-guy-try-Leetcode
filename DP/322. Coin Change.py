class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        可怜的脑子的里只有一维没有多维
        i -> coins[i]
        j : current amount
        dp[i][j] = min(dp[i][j],dp[i][j-coins[i]]+1)
        Runtime: 1977 ms, faster than 52.74% of Python3 online submissions for Coin Change.
        Memory Usage: 14.2 MB, less than 50.02% of Python3 online submissions for Coin Change.
        """
        dp = [float("inf") for i in range(amount+1)]
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(len(dp)):
                # To aviod list index out of range
                if j-coins[i] >=0:
                    dp[j] = min(dp[j],dp[j-coins[i]]+1)
        if dp[-1] == float("inf"):
            return -1
        return dp[-1]
                

if __name__=="__main__":
    coins = [2147483647]
    amount = 2
    a = Solution()
    print(a.coinChange(coins,amount))