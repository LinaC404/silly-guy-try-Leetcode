class Solution(object):
    def mymaxPower(self, s):
        """
        :type s: str
        :rtype: int
        Runtime: 28 ms, faster than 85.44% of Python online submissions for Consecutive Characters.
        Memory Usage: 13.7 MB, less than 10.68% of Python online submissions for Consecutive Characters.
        """
        res = 1
        i = 1
        while i<=len(s)-1:
            if s[i] == s[i-1]:
                temp = 1
                j = i
                while j<=len(s)-1:
                    if s[j]==s[i-1]:
                        temp = temp+1
                        j = j+1
                    else:
                        break
                res = max(res,temp)
                i = j
            else:
                i = i+1
        return res

    def maxPower(self, s):
        res = ct =1
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                res = max(res,ct)
            else:
                ct = ct+1
        return max(res,ct)
    
s = "ccbccbb"
a = Solution()
a.maxPower(s)
