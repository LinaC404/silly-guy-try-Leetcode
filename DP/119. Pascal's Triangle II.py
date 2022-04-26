class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        Runtime: 39 ms, faster than 8.85% of Python online submissions for Pascal's Triangle II.
        Memory Usage: 13.5 MB, less than 14.41% of Python online submissions for Pascal's Triangle II.
        """
        stack = [1]
        level = 2
        while level<=rowIndex+1:
            next_stack = [0 for i in range(level)]
            for i in range(len(stack)):
                if next_stack[i] == 0:
                    next_stack[i] = stack[i]
                else:
                    next_stack[i] += stack[i]
                next_stack[i+1] = stack[i]
            stack = next_stack 
            level += 1
           
        return stack

    def getRow1(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        Runtime: 44 ms, faster than 5.84% of Python online submissions for Pascal's Triangle II.
        Memory Usage: 13.5 MB, less than 38.14% of Python online submissions for Pascal's Triangle II.
        """
        top = [1]
        for i in range(1, rowIndex + 2):
            current = []
            for j in range(0, i):
                if(j == 0 or j == i - 1):
                    current.append(1)
                else:
                    current.append(top[j-1] + top[j])
            top = current
        return top
if __name__=="__main__":
    a = Solution()
    print(a.getRow(4))