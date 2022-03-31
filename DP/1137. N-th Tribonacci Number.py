class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        Runtime: 29 ms, faster than 26.31% of Python online submissions for N-th Tribonacci Number.
        Memory Usage: 13.2 MB, less than 85.30% of Python online submissions for N-th Tribonacci Number.
        """
    
        fib_d = {}
        def cal(n):
            if n in fib_d:
                return fib_d[n]
            if n==0:
                return 0
            if n==1:
                return 1
            if n==2:
                return 1
            fib_d[n] = cal(n-1)+cal(n-2)+cal(n-3)
            return fib_d[n]
        return(cal(n))
            


        
if __name__=="__main__":
    a = Solution()
    print(a.tribonacci(25))