class Solution(object):

    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        Copy & Paste
        https://blog.csdn.net/fuxuemingzhu/article/details/82961114
        2^100 = 2^50*2^2
        先求幂再取模，与先取模再求幂得到的结果是一样的。
        """
        def pow(m, n):
            if n==0 or m==1 : return 1
            if n % 2==1:
                return m * pow(m, n - 1) % 1337
            return pow((m*m)% 1337, n/2) % 1337
            # return m*pow(m, n/2) % 1337 

        res = 1
        for i in b:
            res = pow(res, 10) * pow(a, i) % 1337
            print(res)
        print(res)
        return res
        

a = Solution()
a.superPow(2,[1,0])   