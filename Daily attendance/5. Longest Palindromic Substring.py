class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
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
    s = "qsdccaba"
    a = Solution()
    print(a.longestPalindrome(s))