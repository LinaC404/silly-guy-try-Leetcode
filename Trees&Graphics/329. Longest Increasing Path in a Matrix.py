class Solution(object):
    
    def mylongestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        Time Limit Exceeded
        135 / 138
        """
        rows = len(matrix)
        cols = len(matrix[0])
        path = [[0 for i in range(cols)] for j in range(rows)]

        def nextpath(i,j,m,n,step):
            if path[m][n]!=0:
                path[i][j]=max(step-1+path[m][n],path[i][j])
                return 
            path[i][j] = max(step,path[i][j])
            print(m,n,step)
            directions = [[0,-1],[0,1],[-1,0],[1,0]]
            for dire in directions:
                nextm,nextn = m+dire[0],n+dire[1]
                if 0<=nextm<rows and 0<=nextn<cols:
                    if matrix[nextm][nextn]>matrix[m][n]:
                        nextpath(i,j,nextm,nextn,step+1)  
        for i in range(rows):
            for j in range(cols):
                nextpath(i,j,i,j,1)
                print(path)
        return 



           
matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
a = Solution()
a.longestIncreasingPath(matrix)
