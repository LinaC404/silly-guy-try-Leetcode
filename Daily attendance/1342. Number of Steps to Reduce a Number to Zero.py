class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        Runtime: 33 ms, faster than 14.08% of Python online submissions for Number of Steps to Reduce a Number to Zero.
        Memory Usage: 13.6 MB, less than 5.46% of Python online submissions for Number of Steps to Reduce a Number to Zero.
        """
        ans = 0
        while num!=0:
            if num%2 == 0:
                num = num//2
            else:
                num = num-1
            ans += 1
        return ans

        """
        count = 0
        while num:
            if num & 1:
                num-=1
            else:
                num = num>>1
            count+=1
        return count
        """


a = Solution()  
print(a.numberOfSteps(num = 123))