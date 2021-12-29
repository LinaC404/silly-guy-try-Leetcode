class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        Runtime: 28 ms, faster than 37.49% of Python online submissions for Generate Parentheses.
        Memory Usage: 13.8 MB, less than 42.42% of Python online submissions for Generate Parentheses.
        
        add '(' at first , before get the full item, len(l)>len(r)
        """
        res = []

        def parenthesis(l,r,item):
            if l+r == 2*n:
                res.append(item)
                return
            if l < n:
                parenthesis(l+1,r,item+'(')
            if  r < l:
                parenthesis(l,r+1,item+')')
            
        parenthesis(0,0,'')
        return res
     
if __name__ == "__main__":
    n = 3
    a = Solution()
    a.generateParenthesis(n)