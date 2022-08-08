class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        Runtime: 23 ms, faster than 100.00% of Python online submissions for Special Binary String.
        Memory Usage: 13.4 MB, less than 100.00% of Python online submissions for Special Binary String.
        """
        i, cnt = 0, 0
        ans = []
        for j in range(len(s)):
            cnt += 1 if s[j] == '1' else -1
            if cnt == 0:
                # as a valid case it starts with '1' and ends with '0' 
                # the subarry should be sorted, too                 
                ans.append('1'+self.makeLargestSpecial(s[i+1:j])+'0')
                i = j+1
        
        return "".join(sorted(ans,reverse=True))
        

if __name__=="__main__":
    a = Solution()
    print(a.makeLargestSpecial(s = "11011000"))