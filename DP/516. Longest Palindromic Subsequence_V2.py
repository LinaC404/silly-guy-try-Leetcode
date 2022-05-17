class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        _N = len(s)
        dp = [[0 for i in range(_N)] for j in range(_N)]
        # 
        for n in range(1,_N+1):
            for i in range(0,_N-n+1):
                j = i+n-1
                if i==j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][_N-1]
    
    def longestPalindromeSubseq2(self, s):
        _N = len(s)
        # start with i len n
        dp0 = [0 for i in range(_N)] 
        # len n-1
        dp1 = [0 for i in range(_N)]
        # len n-2
        dp2 = [0 for i in range(_N)]

        for n in range(1,_N+1):
            for i in range(0,_N-n+1):
                j = i+n-1
                if i==j:
                    dp0[i] = 1
                elif s[i]==s[j]:
                    dp0[i] = dp2[i+1] + 2
                else:
                    dp0[i] = max(dp1[i+1],dp1[i])

            dp0,dp1,dp2= dp2,dp0,dp1
 
        return dp1[0] 


if __name__ == "__main__":
    a = Solution()
    print(a.longestPalindromeSubseq(s = "bbbab"))