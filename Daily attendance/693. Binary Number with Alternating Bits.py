class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        Runtime: 20 ms, faster than 73.12% of Python online submissions for Binary Number with Alternating Bits.
        Memory Usage: 13.4 MB, less than 24.73% of Python online submissions for Binary Number with Alternating Bits.
        """
        m = bin(n)
        for i in range(2,len(m)):
            if i%2==0 and m[i]=='1':
                continue
            if i%2==1 and m[i]=='0':
                continue
            return False
        return True
    def hasAlternatingBits2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #  alternating bits, which means the XOR result of n and n>>1 is 1 on each bit.
        a = n ^ (n >> 1)
        return (a & (a+1)) == 0
if __name__=="__main__":
    a = Solution()
    print(a.hasAlternatingBits2(n=10))