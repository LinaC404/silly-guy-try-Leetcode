class Solution(object):
    def mynumDecodings(self, s):
        """
        :type s: str
        :rtype: int
        Runtime: 61 ms, faster than 17.97% of Python3 online submissions for Decode Ways.
        Memory Usage: 14 MB, less than 45.93% of Python3 online submissions for Decode Ways.
        """
        if s[0] == '0': return 0
        if len(s)==1: return 1
        chars = set([str(i) for i in range(1,27)])
        dp = [0 for i in range(len(s))]
        dp[0] = 1
        if s[0]+s[1]=='10' or s[0]+s[1]=='20':
            dp[1] = 1
        elif 11<=int(s[0]+s[1])<=26:
            dp[1] = 2
        elif s[1]=='0':
            dp[0]=0
        else:
            dp[1] = 1
        if len(s) == 2: return dp[1]

        for i in range(2,len(s)):
            if s[i-1]+s[i] in chars and s[i]!='0':
                dp[i] = dp[i-1]+dp[i-2]
            elif s[i-1]+s[i] in chars and s[i]=='0':
                dp[i] = dp[i-2]
            elif s[i-1]+s[i] not in chars and s[i]=='0':
                return 0
            elif s[i-1]+s[i] not in chars and s[i]!='0':
                dp[i] = dp[i-1]
        return dp[-1]
       
       
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if i != 1 and '09' < s[i-2:i] < '27':
                dp[i] += dp[i-2]
        return dp[-1]



if __name__=="__main__":
    a = Solution()
    print(a.numDecodings(s="11"))
