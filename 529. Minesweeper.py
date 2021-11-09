class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        rows,cols = len(board),len(board[0])
        bomb = 0
        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        r_click,c_click = click[0],click[1]
        # print(board[r_click][c_click],click)
        if board[r_click][c_click] == 'M':
            board[r_click][c_click] = 'X'
            return board
        if board[r_click][c_click] != 'M' and board[r_click][c_click] != 'E':
            # print("STR")
            # print(board)
            return
        else:
            nextlist = []
            for dire in directions:
                nexti,nextj = r_click+dire[0],c_click+dire[1]
                if 0<=nexti<rows and 0<=nextj<cols:
                    nextlist.append([nexti,nextj])
                    if board[nexti][nextj] == 'M':
                        bomb = bomb + 1
            board[r_click][c_click] = 'B' if bomb==0 else str(bomb)
            if board[r_click][c_click] == 'B':
                for next_dire in nextlist:
                    nexti,nextj = next_dire[0],next_dire[1]
                    self.updateBoard(board,[nexti,nextj])
        return board

            

        
if __name__=="__main__":
    board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
    click = [3,0]
    a = Solution()
    print(a.updateBoard(board,click))