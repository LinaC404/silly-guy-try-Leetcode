import math
from turtle import st
class Solution(object):
    def myconvert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        Runtime: 580 ms, faster than 7.41% of Python3 online submissions for Zigzag Conversion.
        Memory Usage: 17.9 MB, less than 5.01% of Python3 online submissions for Zigzag Conversion.
        """
        if numRows == 1: return s
        cols = math.ceil(len(s)*(numRows-1)/(2*numRows-2))
        matrix = [["" for i in range(cols)]for j in range(numRows)]
        m=0
        for j in range(cols):
            if m>=len(s):
                break
            flag = j%(numRows-1)
            if flag==0:
                for i in range(numRows):
                    if m>=len(s):
                        break
                    matrix[i][j] = s[m]
                    m += 1 
            else:
                matrix[numRows-flag-1][j] = s[m]
                m += 1
        ans = ""
        for i in matrix: 
            ans += "".join(i)
        return ans
    
    def convert(self, s: str, numRows: int) -> str:
        """
        Runtime: 96 ms, faster than 42.58% of Python3 online submissions for Zigzag Conversion.
        Memory Usage: 13.8 MB, less than 98.16% of Python3 online submissions for Zigzag Conversion.
        """
        if numRows == 1 or numRows >= len(s):
            return s
 
        # [''] ⇩   ⇩
        # [''] ⇩ ⇧ ⇩
        # [''] ⇩   ⇩
        L = [''] * numRows
        index, step = 0, 1
        for x in s:
            L[index] += x
            # ⇩　head
            if index == 0:
                step = 1
            # ⇧　tail
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
    

if __name__=="__main__":
    s = "ABCDEFGHI"
    numRows = 3
    a = Solution()
    print(a.convert(s,numRows))