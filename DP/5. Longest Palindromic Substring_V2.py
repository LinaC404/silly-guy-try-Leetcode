class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        Runtime: 879 ms, faster than 71.72% of Python online submissions for Longest Palindromic Substring.
        Memory Usage: 13.7 MB, less than 48.10% of Python online submissions for Longest Palindromic Substring.
        """
        self.ans = s[0]

        def checker(i,j):
            while i>=0 and j<=len(s)-1:
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                else:
                    break
            subarray = s[i+1:j]
            if len(subarray) > len(self.ans):
                self.ans = subarray

        for i in range(1,len(s)):
                sub1 = checker(i,i)
                sub2 = checker(i-1,i)
        return self.ans

if __name__ == "__main__":
    a = Solution()
    print(a.longestPalindrome(s = "ccc"))