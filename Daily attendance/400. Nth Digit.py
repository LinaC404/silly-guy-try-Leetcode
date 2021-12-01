import math
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        Runtime: 12 ms, faster than 91.30% of Python online submissions for Nth Digit.
        Memory Usage: 13.3 MB, less than 78.26% of Python online submissions for Nth Digit.
        """
        i = 1
        _len = 9
        temp = i*_len
        m = _len
        while temp<n:
            i = i+1
            _len = _len*10
            temp = temp+i*_len
            m = m + _len
        temp = temp-i*_len
        m = m-_len
        cur_num =  int(math.modf((n-temp)/i)[1])
        a = (n-temp)%i
        if a == 0:
            res = cur_num+m
            return str(res)[-1]
        else:
            res = cur_num+m+1
            return str(res)[a-1]