import math
class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        Primechecker:https://zhuanlan.zhihu.com/p/107300262
        Runtime: 17 ms, faster than 93.94% of Python online submissions for Prime Arrangements.
        Memory Usage: 13.4 MB, less than 57.58% of Python online submissions for Prime Arrangements.
        """
        if n==1: return 1
        def prime(n):
            count = 0 if n<2 else 1
            for i in range(3,n+1):
                is_prime = True
                if i%2==0:
                    continue
                for j in range(2,int(i**0.5)+1):
                    if i%j==0:
                        is_prime = False
                if is_prime:
                    count += 1
            return count

        primes = prime(n)
        return (math.factorial(primes)*math.factorial(n-primes))%1000000007
        
if __name__=="__main__":
    a = Solution()
    print(a.numPrimeArrangements(100))