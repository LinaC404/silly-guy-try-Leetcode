class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        """
        :type p: str
        :rtype: int
        Runtime: 132 ms, faster than 51.69% of Python3 online submissions for Unique Substrings in Wraparound String.
        Memory Usage: 14 MB, less than 79.71% of Python3 online submissions for Unique Substrings in Wraparound String.
        """
        ans = len(p)
        dp = [0 for i in range(26)]
        dp[ord(p[0])-97] = 1
        _L = 1
        for i in range(1,len(p)):
            pre,curr = ord(p[i-1])-97, ord(p[i])-97
            if curr-pre==1 or curr-pre==-25:
                _L += 1
            else:
                _L = 1
            dp[curr] = max(dp[curr],_L)
        return sum(dp)
            
            

if __name__=="__main__":
    p = "abmmmabcdef"
    a = Solution()
    print(a.findSubstringInWraproundString(p))