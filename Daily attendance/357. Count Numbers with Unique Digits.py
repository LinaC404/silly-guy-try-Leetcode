class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        Runtime: 16 ms, faster than 91.78% of Python online submissions for Count Numbers with Unique Digits.
        Memory Usage: 13.3 MB, less than 73.97% of Python online submissions for Count Numbers with Unique Digits.
        """
        if n==0: return 0
        if n==1: return 10
        li = [9,9,8,7,6,5,4,3,2,1,0]

        res = 10
        for i in range(2,n+1):
            temp = 1
            for j in range(i):
                temp *= li[j]
            res += temp
        return res

        
if __name__=="__main__":
    a = Solution()
    print(a.countNumbersWithUniqueDigits(8))