class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n<3:
            return []

        def dfs(curr,k,n,temp):
            if k==0:
                if n==0:
                    # 注意值的深拷贝 浅拷贝
                    res.append(temp[:])
                return

            for i in range(curr,10):                
                if i>n:
                    return
                temp.append(i)
                dfs(i+1,k-1,n-i,temp)
                temp.pop()
            

        res = []
        dfs(1,k,n,[])
        return res


if __name__=="__main__":
    k = 3
    n = 9
    a = Solution()
    a.combinationSum3(k,n)



