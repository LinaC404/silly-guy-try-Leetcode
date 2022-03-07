class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        Runtime: 30 ms, faster than 32.35% of Python online submissions for Base 7.
        Memory Usage: 13.6 MB, less than 17.65% of Python online submissions for Base 7.
        """
        if num == 0: return '0'
        res = ""
        flag = "-" if num<0 else ""
        num = abs(num)
        while num != 0:
            a,b = divmod(num,7)
            res += str(b)
            num = a
        return flag+"".join(res[::-1])
        
if __name__=="__main__":
    num = 10003
    a = Solution()
    print(a.convertToBase7(num))