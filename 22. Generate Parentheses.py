class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def choices(num,flag,res):
            if num == n*2:
                res.append(flag)
                return res
            else:
                for i in range(2):
                    choices(num+1,flag+str(i),res)

        def counter(res):
            reslist = []
            stack = []
            dic = {'0':'(','1':')'}
            for i in range(len(res)):
                stack = []
                stack.append(res[i][0])
                for j in range(1,len(res[i])):
                    stack.append(res[i][j])
                    if len(stack) == 1:
                        pass
                    elif stack[-2] == '0' and stack[-1]  == '1':
                        stack.pop()
                        stack.pop()
                if len(stack) == 0:
                    temp = ''
                    for m in range(len(res[i])):
                        temp = temp + dic[res[i][m]]
                    reslist.append(temp)
            return reslist


        if n == 0:
            return ['']
        if n == 1:
            return ['()']

        res = []
        choices(0,'',res)
        # print(res)
        for i in range(len(res)):
            flag0 = 0
            flag1 = 0
            for j in res[i]:
                if j == '0':
                    flag0 = flag0 + 1
                else:
                    flag1 = flag1 + 1
            if flag0 != flag1:
                res[i] = 0
        for i in range(len(res)-1,-1,-1):
            if res[i] == 0:
                res.pop(i)
        return(counter(res))            

if __name__  == "__main__":
    n = 3
    a = Solution()
    print(a.generateParenthesis(n))