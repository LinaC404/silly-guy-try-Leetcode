class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        Runtime: 45 ms, faster than 85.82% of Python3 online submissions for Shortest Distance to a Character.
        Memory Usage: 14 MB, less than 57.93% of Python3 online submissions for Shortest Distance to a Character.
        """
        res = []
        mark = []
        for i in range(len(s)):
            if s[i] == c:
                res.append(0)
                mark.append(i)
            else:
                res.append(-1)

        if len(mark)==1:
            l = r = mark[0]
        else:
            f = 0
            l,r=mark[f],mark[f+1]
        for i in range(len(s)):
            if r!= mark[-1] and abs(i-l)>=abs(i-r):
                f += 1 
                l = r
                r = mark[f]
            res[i] = min(abs(l-i),abs(r-i))
        return res

    def shortestToChar2(self, s, c):
        prev = float('-inf')
        ans = []
        for i, x in enumerate(s):
            if x == c:
                prev = i
            ans.append(i-prev)
        after = float('inf')
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                after = i
            ans[i] = min(ans[i], after-i)
        return ans


            
        
if __name__=="__main__":
    s = "loveleetcode"
    c = "e"
    a = Solution()
    print(a.shortestToChar2(s,c))