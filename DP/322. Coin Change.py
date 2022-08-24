class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float("inf") for i in range(amount+1)]
        for c in coins:
            if c <= amount:
                dp[c] = 1
        for i in range(len(dp)):
            for c in coins:
                if i-c>=0:
                    dp[i] = min(dp[i],dp[i-c]+1)
        return dp[-1]

        

if __name__=="__main__":
    a = Solution()
    coins = [1,2,5]
    amount = 11
    print(a.coinChange(coins,amount))
