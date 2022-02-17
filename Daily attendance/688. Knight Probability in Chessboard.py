class Solution(object):
    def knightProbability1(self, n, k, row, column):
        """
        TLE 11/22
        """
        directions = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]
        in_board = 0
        total = 1
        def dfs(times,px,py,all):
            if times == k:
                in_board += 1
                total = all
                return
            for i,j in directions:
                nexti,nextj = px+i,py+j
                if 0<=nexti<=n-1 and 0<=nextj<=n-1:
                    dfs(times+1,nexti,nextj,all*8)
        dfs(0,row,column,1)
        return in_board/total

    def knightProbability(self, n, k, row, column):
        """
        Runtime: 357 ms, faster than 60.93% of Python3 online submissions for Knight Probability in Chessboard.
        Memory Usage: 14 MB, less than 90.56% of Python3 online submissions for Knight Probability in Chessboard.
        """
        state = [[0 for i in range(n)] for j in range(n)]
        state[row][column] = 1
        directions = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]      

        for t in range(k):
            # current layer, next layer ->　cover the previous layer 
            next_state = [[0 for i in range(n)] for j in range(n)]
            for px in range(n):
                for py in range(n):
                    for i,j in directions:
                        nexti,nextj = px+i,py+j
                        if 0<=nexti<=n-1 and 0<=nextj<=n-1:
                            next_state[nexti][nextj] += state[px][py]
            state = next_state
        return sum(map(sum,state))/(8**k)


        
if __name__ == "__main__":
    n = 3
    k = 2
    row = 0
    column = 0
    a = Solution()
    print(a.knightProbability( n, k, row, column))