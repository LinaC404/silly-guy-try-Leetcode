class Solution(object):
    def myrepeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        49 / 57 test cases passed.
        """
        ans = 0
        if a==b or a.find(b)!=-1: return 1
        i = b.find(a)
        if i == -1:
            return -1
        else:
            if i!=0 and b[:i] != a[-i:]:
                return -1
            if i != 0:
                ans += 1
            index = 0
            for j in range(i,len(b)):
                if b[j]!=a[index%len(a)]: return -1
                if index%len(a) == 0:
                    ans += 1
                index += 1
        return ans     
        
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        当A重复一定次数后，长度比B长了，那么就可以停止了
        因为如果这种情况下B都不是A的子串，那么循环再多也没用。
        因为对于B来说，A所有可能的重复都已经出现了。
        头尾+1  range +1 ->+3
        times:2
        Runtime: 104 ms, faster than 55.17% of Python online submissions for Repeated String Match.
        Memory Usage: 13.9 MB, less than 44.83% of Python online submissions for Repeated String Match.
        """
        _a,_b = len(a),len(b)
        times = int(_b/_a)+3
        print(times)
        for j in range(1,times):
            if b in a*j:
                return j
        return -1
if __name__=="__main__":
    a = "aa"
    b = "a"
    c = Solution()
    print(c.repeatedStringMatch(a,b))