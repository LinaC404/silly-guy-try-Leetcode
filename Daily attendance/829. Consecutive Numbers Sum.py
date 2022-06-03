class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        # consecutive Number    start+1,start+1,...,start+k
        #                len    k
        #                sum    start*k + k*(k+1)/2    
        #         find legal    start = (n-k*(k+1)/2)/k

        ans = 1
        
        k = 2
        # the length starts with 2
        while k*(k+1)/2 <= n:
            if (n-k*(k+1)/2)%k==0:
                ans += 1
                print(k,(n-k*(k+1)/2)/k)
            k += 1
            
        return ans


if __name__=="__main__":
    n = 15
    a = Solution()
    print(a.consecutiveNumbersSum(n))