class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ans = 0 
        strs =  list(zip(*strs))
        for i in range(len(strs)):
            if list(strs[i]) != sorted(strs[i]):
                ans+=1
        return ans

        
if __name__=="__main__":
    a = Solution()
    print(a.minDeletionSize(["rrjk","furt","guzm"]))