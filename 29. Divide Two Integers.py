class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = 0
        flag = 0
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            flag = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend>=divisor:
            n = 0
            while dividend >= divisor<<n:
                # print(n)
                n = n+1
            result += 1<<(n-1)
            print(result)
            dividend = dividend - (divisor<<(n-1))
            print(dividend)
        if flag<0:
            result = -result
        if result>2147483648 or result<-2147483647:
            return 2147483647

        return result

        
if __name__ == "__main__":
    dividend = 500
    divisor = 37
    a = Solution()
    print(a.divide(dividend,divisor))