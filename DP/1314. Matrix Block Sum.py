class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        _N = len(mat)
        _M = len(mat[0])
        presum = [[0 for i in range(_M)] for j in range(_N)]      
        # get the presum
        for i in range(_N):
            all = 0
            for j in range(_M):
                all += mat[i][j]
                presum[i][j] = all
                if i>0:
                   presum[i][j] += presum[i-1][j]
        # Cal the sum
        ans = [[0 for i in range(_M)] for j in range(_N)]      
        for i in range(_N):
            for j in range(_M):
                x1,x2 = max(0,i-k),min(i+k,_N-1) 
                y1,y2 = max(0,j-k),min(j+k,_M-1)
                ans[i][j] = presum[x2][y2]
                if x1>0: ans[i][j] -= presum[x1-1][y2]
                if y1>0: ans[i][j] -= presum[x2][y1-1]
                if x1>0 and y1>0: ans[i][j] += presum[x1-1][y1-1]
        return ans



if __name__=="__main__":
    a = Solution()
    print(a.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1))