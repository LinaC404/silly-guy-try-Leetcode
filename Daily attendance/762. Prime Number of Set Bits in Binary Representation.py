from math import sqrt
class Solution(object):
    def mycountPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        Runtime: 1016 ms, faster than 30.67% of Python online submissions for Prime Number of Set Bits in Binary Representation.
        Memory Usage: 13.9 MB, less than 20.00% of Python online submissions for Prime Number of Set Bits in Binary Representation.
        """
        res = 0
        for i in range(left,right+1):
            c = bin(i)[2:]
            count = 0
            for j in c:
                if j=="1":
                    count += 1
            if count > 1:
                mark = 0
                for i in range(2,int(sqrt(count)+1)):
                    if count%i == 0:
                        mark = 1
                        break
                if mark==0:
                    res+=1
        return res
    def countPrimeSetBits(self, left, right):
        """
        1 <= left <= right <= 10e6
        Runtime: 169 ms, faster than 90.67% of Python online submissions for Prime Number of Set Bits in Binary Representation.
        Memory Usage: 13.6 MB, less than 90.67% of Python online submissions for Prime Number of Set Bits in Binary Representation.
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        res = 0
        for i in range(left, right + 1):
            if bin(i).count('1') in primes:
                res += 1
        return res
    
a = Solution()
print(a.countPrimeSetBits(6,10))