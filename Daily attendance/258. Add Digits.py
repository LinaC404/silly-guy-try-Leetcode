class Solution(object):
    def myaddDigits(self, num):
        """
        :type num: int
        :rtype: int
        Runtime: 32 ms, faster than 40.98% of Python online submissions for Add Digits.
        Memory Usage: 13.4 MB, less than 64.52% of Python online submissions for Add Digits.
        """
        if len(num)==1: return num
        while len(str(num))>1:
            temp = 0
            for i in str(num):
                temp += int(i)
            num = temp
        return temp
    def addDigits(self, num):
        """
        https://en.wikipedia.org/wiki/Digital_root
        Runtime: 28 ms, faster than 56.02% of Python online submissions for Add Digits.
        Memory Usage: 13.3 MB, less than 85.50% of Python online submissions for Add Digits.
        """
        return(num-1)%9+1

        
        
if __name__=="__main__":
    num = 388
    a = Solution()
    print(a.addDigits(num))
