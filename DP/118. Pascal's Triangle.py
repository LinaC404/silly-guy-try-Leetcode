class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        Runtime: 28 ms, faster than 30.41% of Python online submissions for Pascal's Triangle.
        Memory Usage: 13.3 MB, less than 63.69% of Python online submissions for Pascal's Triangle.
        """
        res = [[1]]
        stack = [1]
        level = 2
        while level<=numRows:
            next_stack = [0 for i in range(level)]
            for i in range(len(stack)):
                if next_stack[i] == 0:
                    next_stack[i] = stack[i]
                else:
                    next_stack[i] += stack[i]
                next_stack[i+1] = stack[i]
            stack = next_stack 
            level += 1
            res.append(next_stack)
        return res
    def generate1(self,numRows):
        """
        Runtime: 23 ms, faster than 52.03% of Python online submissions for Pascal's Triangle.
        Memory Usage: 13.3 MB, less than 86.98% of Python online submissions for Pascal's Triangle.
        """
        res=[[1]*(i+1) for i in range(numRows)]
        for i in range(2,numRows):
            for j in range(1,i):
                res[i][j]=res[i-1][j-1]+ res[i-1][j]
        
        return res

        
if __name__=="__main__":
    a = Solution()
    print(a.generate1(5))
