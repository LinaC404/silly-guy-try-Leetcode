class Solution(object):
    def integerReplacement1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n%2 == 0:
            return self.integerReplacement(n/2)+1
        else:
            return min(self.integerReplacement(n-1),self.integerReplacement(n+1))+1
    def integerReplacement(self, n):
        """
        二进制的奇数以1结尾  01 11

        如果数是4的倍数步骤减少 （3例外）

        01->-1               11->+1
        """
        res = 0
        while n >1:
            print(n)
            # odd
            if n%2==1:
                # 11&10 ->1(+1) 01&10 ->0(-1)
                if n&2 and n!=3:
                    n = n+1
                else:
                    n = n-1
            else:
                n = int(n/2)
            res = res + 1

        return res
            




        
if __name__ == "__main__":
    n = 65533
    a = Solution()
    a.integerReplacement(n)