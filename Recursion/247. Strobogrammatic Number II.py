class Solution(object):
    def myfindStrobogrammatic(self, n):
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

    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        Runtime: 162 ms, faster than 72.73% of Python online submissions for Strobogrammatic Number II.
        Memory Usage: 24 MB, less than 68.60% of Python online submissions for Strobogrammatic Number II.
        The better code 
        """
        def inner(x,y):
            #  return "" whenn is even/ return ["0","1","8"] when n is odd
            if x == 0: return [""]
            if x == 1: return ["0","1","8"]
            
            # I almost did not use return ans like it
            partial = inner(x-2,y)
            
            ret = []
            
            for one_combo in partial:
                # To avoid add 0 at the beginning of string
                if x != y: ret.append("0{}0".format(one_combo))
                ret.append("1{}1".format(one_combo))
                ret.append("6{}9".format(one_combo))
                ret.append("9{}6".format(one_combo))
                ret.append("8{}8".format(one_combo))
            return ret

        return inner(n,n)


if __name__=="__main__":
    n = 3
    a = Solution()
    print(a.findStrobogrammatic(n))
