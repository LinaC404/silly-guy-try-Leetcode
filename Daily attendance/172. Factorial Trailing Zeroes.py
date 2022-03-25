class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        https://www.cnblogs.com/grandyang/p/4219878.html
        """
        # be careful ablout 5*5 5*5*5 ...         
        res = 0
        while n>0:
            res += n//5
            n = n//5
        return res
        
if __name__=="__main__":
    n = 125
    a = Solution()
    print(a.trailingZeroes(n))
