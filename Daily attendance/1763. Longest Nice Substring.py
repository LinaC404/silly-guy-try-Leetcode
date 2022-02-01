class Solution(object):
    def mylongestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        Runtime: 300 ms
        Memory Usage: 13.7 MB
        """
        ans = ""
        if len(s) == 1: return ans
        def nice(substr):
            sub_str = list(substr)
            tar_str = list(substr.swapcase())
            for c in tar_str:
                if c not in sub_str:
                    return False
            return True

        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if nice(s[i:j+1]) and len(s[i:j+1])>len(ans):
                    ans = s[i:j+1]
        return ans

    def longestNiceSubstring(self, s):
        """
        Runtime: 20 ms
        Memory Usage: 13.9 MB
        """
        if not s: return "" # boundary condition 
        ss = set(s)
 
        for i, c in enumerate(s):
            # divide the subarray based on the element s[:i] i s[i+1:]
            if c.swapcase() not in ss: 
                s0 = self.longestNiceSubstring(s[:i])
                s1 = self.longestNiceSubstring(s[i+1:])
                return max(s0, s1, key=len)
        return s

a = Solution()
print(a.longestNiceSubstring(s = "dDzeE"))