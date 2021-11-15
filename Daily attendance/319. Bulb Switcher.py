class Solution(object):
    def bulbSwitch(self, n=99999999):
        """
        首先想到暴力法，n <= 10^9 ,肯定会时间超限的 O(N^2)
        > 分解成 组成一个整数的素数的个数，双数 off,单数 on,但求素数依然不能减少时间复杂度
        > https://baihuqian.github.io/2018-07-31-bulb-switcher/
        参考该blog,     
        12 (1,12) (2,6) (3,4)  (4,3) (6,2) (12,1)
            ----------------   -----------------
        25 (1,25) (5,5) (25,1)
           ------        ------
             on    off    on
        36 (1,36) (2,18) (3,12) (4,9) (6,6) (36,1) (18,2) (12,3) (9,4)
           --------------------------       -------------------------- (两边相抵)
             on    off     on    off    on    off    on     off    on
        > 除了i*i 没有对应的数与之抵消，其它都为 off  --> 题目转换成存在几个i*i

        :type n: int
        :rtype: int
        """
        ans = 0
        if n==0: return ans
        flag = 1
        while flag*flag <= n:
            flag = flag+1
            ans = ans + 1
        return ans
        
a = Solution()
a.bulbSwitch()