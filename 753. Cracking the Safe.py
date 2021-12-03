class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        1 <= n <= 4
        1 <= k <= 10 (0~9)
        1 <= k^n <= 4096
        抄的，做不来
        https://zxi.mytechroad.com/blog/graph/leetcode-753-cracking-the-safe/
        https://blog.csdn.net/fuxuemingzhu/article/details/82945477
        Runtime: 40 ms
        Memory Usage: 17.4 MB
        
        """

        # 1.　初始所有密码的长度n*k^n
        # 2.　(n-1)位密码被重复使用，(n-1)*(k^n-1),最后一个密码不重复使用
        # 2.-1. -> 密码的长度应该为  k**n + n -1
        # /visited 长度为 K**n 也可作为结束dfs的条件
        _total_len = k**n+n-1
        # 初始化一个密码
        ans = ["0"] * n
        # 记录已经查找过的password
        visited = set()
        visited.add("".join(ans))
        if self.dfs(ans,_total_len,n,k,visited):
            return "".join(ans)
        return ""

    def dfs(self,ans,_total_len,n,k,visited):
        if len(ans) == _total_len:
            return True
        password = "".join(ans[len(ans)-n+1:])

        for i in range(k):
            password += str(i)
            if password not in visited:
                ans.append(str(i))
                visited.add(password)
                if self.dfs(ans,_total_len,n,k,visited):
                    return True
                ans.pop()
                visited.remove(password)
            password = password[:-1]




if __name__=="__main__":
    n = 2 
    k = 2
    a = Solution()
    a.crackSafe(n,k)

        