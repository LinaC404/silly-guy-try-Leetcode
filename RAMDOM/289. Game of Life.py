class MySolution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        state = [[0 for i in range(n)] for j in range(m)]
        print(state)
        for i in range(m):
            for j in range(n):
                live_neigh = 0
                directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
                for dire in directions:
                    neigh_x = i + dire[0]
                    neigh_j = j + dire[1]
                    if neigh_x < 0 or neigh_j < 0 or neigh_x > m-1 or neigh_j > n-1:
                        pass
                    else:
                        if board[neigh_x][neigh_j] == 1:
                            live_neigh = live_neigh + 1

                if board[i][j] == 1:
                    if live_neigh < 2:
                        state[i][j] = 1
                    elif live_neigh > 3:
                        state[i][j] = 1
                elif board[i][j] == 0:
                    if live_neigh == 3:
                        state[i][j] = 1

        for i in range(m):
            for j in range(n):
                if state[i][j] == 1:
                    if board[i][j] == 1:
                        board[i][j] = 0
                    else:
                        board[i][j] = 1
        return board

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        """
        IN-PLACE
        XY X: next state, Y: current state 
                    Y     XY   decimal
        board[0][0] 0 --> 00      0
        board[0][1] 1 --> 01      1
        board[1][0] 0 --> 10      2
        board[2][1] 1 --> 11      3
        
        * check the current status (1,1->return 1) board[i][j] & 1
        
        * return next status board[i][j] >>= 1
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                live_neigh = 0
                directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
                for dire in directions:
                    neigh_x,neigh_j = i + dire[0],j + dire[1]
                    if m> neigh_x >=0 and n> neigh_j >=0:
                        if board[neigh_x][neigh_j] & 1:
                            live_neigh = live_neigh + 1
                
                if board[i][j] == 0:
                    if live_neigh == 3:
                        board[i][j] = 2
                else:
                    if 2<=live_neigh<=3:
                        board[i][j] = 3
                    
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j]>>1
        return board

      
if __name__=="__main__":
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    a = Solution()
    a.gameOfLife(board)
