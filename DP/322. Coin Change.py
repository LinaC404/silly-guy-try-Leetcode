class Solution(object):
    def coinChange1(self, coins, amount):
        """
        https://www.youtube.com/watch?v=uUETHdijzkA
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
    
    def coinChange2(self, coins, amount):
        """
        TLE 
        ?
        """
        # DFS + greedy + pruning(cut down time)
        self.res = float("inf")
        coins = sorted(coins,reverse=True)
        
        def dfs(idx,amount,count):
            if amount == 0:
                self.res = count
                return
            if idx == len(coins):
                return

            print(coins[idx],amount,count)
            coin = coins[idx]
            for j in range(amount//coin,-1,-1):
                if count+j>self.res:
                    break
                dfs(idx+1,amount-j*coin,count+j)
        dfs(0,amount,0)
        return -1 if self.res==float("inf") else self.res

if __name__=="__main__":
    coins = [2147483647]
    amount = 2
    a = Solution()
    print(a.coinChange(coins,amount))
