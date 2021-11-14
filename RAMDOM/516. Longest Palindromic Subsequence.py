class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
                print(dp)
        return dp[0][len(s)-1]
        
if __name__=="__main__":
    s = "bbbab"
    a = Solution()
    print(a.longestPalindromeSubseq(s))