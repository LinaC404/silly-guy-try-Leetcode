class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        li = [str(i) for i in range(1,n+1)]
        li = sorted(li)
        return [int(i) for i in li]

        

if __name__=="__main__":
    a = Solution()
    print(a.lexicalOrder(n=13))
        