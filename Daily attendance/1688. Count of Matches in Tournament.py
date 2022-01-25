class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        res = 0
        while n!=1:
            if n%2 == 0:
                match = n/2
                n = match
            else:
                match = (n-1)/2
                n = match+1
            res += match
        return int(res)
        # return n-1
        
if __name__=="__main__":
    a = Solution()
    a.numberOfMatches(n=7)