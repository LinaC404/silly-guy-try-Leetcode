class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        Runtime: 137 ms, faster than 60.00% of Python online submissions for Minimum Falling Path Sum.
        Memory Usage: 14.4 MB, less than 28.21% of Python online submissions for Minimum Falling Path Sum.
        """
        if len(matrix)==1: return min(matrix[0])
        for i in range(1,len(matrix)):
            temp = matrix[i][:]
            for j in range(len(matrix[i])):
                li = [(i-1,j-1),(i-1,j),(i-1,j+1)]
                curr = float("inf")
                for pre in li:
                    if 0<=pre[1]<len(matrix[0]):
                        curr = min(curr,matrix[pre[0]][pre[1]])
                temp[j] = matrix[i][j] + curr
                matrix[i] = temp
        return min(temp)


        
if __name__=="__main__":
    a = Solution()
    print(a.minFallingPathSum(matrix = [[2,1,3],[6,5,4],[7,8,9]]))