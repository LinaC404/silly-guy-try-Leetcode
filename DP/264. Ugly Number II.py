class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        Runtime: 182 ms, faster than 53.07% of Python online submissions for Ugly Number II.
        Memory Usage: 13.6 MB, less than 45.61% of Python online submissions for Ugly Number II.
        """
        res = [1]
        i2,i3,i5 = 0,0,0
        i = 1
        while i<n:
            cur = min(res[i2]*2,res[i3]*3,res[i5]*5)
            res.append(cur)
            i2 +=1 if cur == res[i2]*2 else 0
            i3 +=1 if cur == res[i3]*3 else 0
            i5 +=1 if cur == res[i5]*5 else 0
            i += 1
        return res[-1]
        
if __name__=="__main__":
    a = Solution()
    print(a.nthUglyNumber(n=11))