class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        Runtime: 22 ms, faster than 69.10% of Python online submissions for Fibonacci Number.
        Memory Usage: 13.6 MB, less than 10.95% of Python online submissions for Fibonacci Number.
        """
        fib_d = {}
        def cal(n):
            if n in fib_d:
                return fib_d[n]
            if n==0:
                return 0
            if n==1:
                return 1
            fib_d[n] = cal(n-1)+cal(n-2)
            return fib_d[n]
        return(cal(n))
            


        
if __name__=="__main__":
    a = Solution()
    print(a.fib(4))