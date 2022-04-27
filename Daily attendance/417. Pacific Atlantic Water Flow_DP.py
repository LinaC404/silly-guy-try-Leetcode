class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        Runtime: 2292 ms, faster than 8.18% of Python3 online submissions for Pacific Atlantic Water Flow.
        Memory Usage: 15.3 MB, less than 99.76% of Python3 online submissions for Pacific Atlantic Water Flow.
        """
        rows = len(heights)
        cols = len(heights[0])
        dp = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            dp[i][0] |= 1
            dp[i][cols-1] |= 2
        for j in range(cols):
            dp[0][j] |= 1
            dp[rows-1][j] |= 2


        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        check = True
        while check:
            check = False
            for i in range(rows):
                for j in range(cols):
                    for dire in directions:
                        prei = i+dire[0]
                        prej = j+dire[1]
                        # no state change, break, so dp[i][j]|dp[prei][prej] == dp[i][j] also should pass
                        if prei<0 or prej<0 or prei>=rows or prej>=cols or heights[i][j]<heights[prei][prej] or dp[i][j]|dp[prei][prej] == dp[i][j]:
                            continue
                        dp[i][j] |= dp[prei][prej]
                        check = True
        
        return [[i,j] for i in range(rows) for j in range(cols) if dp[i][j]==3]


if __name__ == "__main__":
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    a = Solution()
    print(a.pacificAtlantic(heights))