class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs = sorted(strs, key=lambda x:-len(x))
        def subCheck(w,t):
            if len(w)>len(t): return False
            i = 0
            for c in t:
                if i<len(w) and w[i]==c:
                    i += 1
            return i==len(w)
        
        for i in range(len(strs)):
            found = True
            for j in range(len(strs)):
                if i==j: continue
                if subCheck(strs[i],strs[j]):
                    found = False
                    break
            if found: return len(strs[i])
        return -1

if __name__=="__main__":
    a = Solution()
    print(a.findLUSlength(strs = ["aaa","aaa","aa"]))