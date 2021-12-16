class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        Runtime: 257 ms, faster than 18.55% of Python online submissions for Strobogrammatic Number II.
        Memory Usage: 26.8 MB, less than 12.10% of Python online submissions for Strobogrammatic Number II.
        """
        
        strs1 = ["0","1","8"]
        strs2 = ["11","69","88","96"]
        if n==1: return strs1
        if n==2: return strs2
        my_dict = {"0":"0","1":"1","6":"9","8":"8","9":"6"}
        def stro(_N,s):
            if _N==self.length:
                res.append(s)
                return
            for char1,char2 in my_dict.items():
                # s = s[:int(len(s)/2)]+char1+char2+s[int(len(s)/2):]
                # print(s)
                stro(_N+2,s[:int(len(s)/2)]+char1+char2+s[int(len(s)/2):])


            
        res = []
        ans = []
        if n%2==0:
            self.length=n
            for s in strs2:
                stro(2,s)
            return res
        # print(res)
        elif n%2==1:
            self.length=n-1
            for s in strs2:
                stro(2,s)
            for j in range(len(res)):
                for m in strs1:
                    ans.append(res[j][:int(len(res[j])/2)]+m+res[j][int(len(res[j])/2):])
            return ans




if __name__=="__main__":
    n = 3
    a = Solution()
    print(a.findStrobogrammatic(n))