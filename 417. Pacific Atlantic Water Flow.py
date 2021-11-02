class Solution(object):
    """
    https://zxi.mytechroad.com/blog/searching/417-pacific-atlantic-water-flow/
    以四条边界为起点，寻找周围大于等于该点的值，降低时间复杂度至线性
    """
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(heights)
        n = len(heights[0])
        T_visited = [[0 for i in range(n)] for j in range(m)]
        L_visited = [[0 for i in range(n)] for j in range(m)]
        res = []


        def findexit(visited,i,j):
            visited[i][j] = 1
            directions = [[0,-1],[0,1],[-1,0],[1,0]]
            for dire in directions:
                nexti,nextj = i+dire[0], j+dire[1]
                if 0<=nexti<=m-1 and 0<=nextj<=n-1 :
                    if heights[nexti][nextj]>=heights[i][j] and visited[nexti][nextj]==0:
                        findexit(visited,nexti,nextj)
        
        for i in range(m):
            findexit(T_visited,i,0)
            findexit(L_visited,i,n-1)
        for j in range(n):
            findexit(T_visited,0,j)
            findexit(L_visited,m-1,j)
        for i in range(m):
            for j in range(n):
                if T_visited[i][j] and L_visited[i][j]:
                    res.append([i,j])
        return res
        
if __name__ == "__main__":
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    a = Solution()
    a.pacificAtlantic(heights)