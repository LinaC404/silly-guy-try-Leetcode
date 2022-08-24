import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf") for i in range(n+1)]
        i = 1
        while i*i<=n:
            dp[i*i] = 1
            i += 1
        for i in range(1,n+1):
            for j in range(int(math.sqrt(i)),0,-1):
                dp[i] = min(dp[i],dp[i-j*j]+1)
                # print(">",i,j,dp[i])
        return dp[-1]


if __name__=="__main__":
    a = Solution()
    print(a.numSquares(12))