class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        Runtime: 284 ms, faster than 87.77% of Python online submissions for Longest Common Subsequence.
        Memory Usage: 22.7 MB, less than 20.93% of Python online submissions for Longest Common Subsequence.
        """
        m = len(text1)
        n = len(text2)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text2[i-1]==text1[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]




if __name__=="__main__":
    a = Solution()
    print(a.longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))