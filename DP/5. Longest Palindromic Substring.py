class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
        Runtime: 906 ms, faster than 83.44% of Python3 online submissions for Longest Palindromic Substring.
        Memory Usage: 14.1 MB, less than 50.10% of Python3 online submissions for Longest Palindromic Substring.
        """
        max_len = 0
        res = ""
        def length(i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i -= 1
                j += 1
            return j-i-1
        for i in range(len(s)):
            curr_len = max(length(i,i),length(i,i+1))
            if curr_len<=max_len: continue
            res = s[i-(curr_len-1)//2:i+(curr_len-(curr_len-1)//2)]
            max_len = curr_len
        return res

# ------------------------------------------------------------------------------------------------------------------
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        TLE
        """
        s = list(s)
        s1 = s[::-1]
        state = [[0 for i in range(len(s))] for j in range(len(s))]
        #          i j len
        len_max = [0,0,0]
        for i in range(len(s1)):
            for j in range(len(s)):
                if s1[i]==s[j]:
                    state[i][j] = state[i-1][j-1]+1 if i-1>=0 and j-1>=0 else 1
                    p = len(s1)-2-j+state[i][j]
                    if state[i][j]>=len_max[2] and p==i:
                        len_max=[i,j,state[i][j]]
        return "".join(s[len_max[1]-len_max[2]+1:len_max[1]+1])
        
if __name__=="__main__":
    s = "babad"
    a = Solution()
    print(a.longestPalindrome(s))