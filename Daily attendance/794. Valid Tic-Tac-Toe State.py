class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        def check(mark):
            # The all() function is an inbuilt function in Python which returns true if all the elements of a given iterable
            # ( List, Dictionary, Tuple, set, etc) are True else it returns False. It also returns True if the iterable object is empty.
            for j in range(3):
                if all(board[j][i] == mark for i in range(3)): return True
                if all(board[i][j] == mark for i in range(3)): return True
            if board[0][0]==board[1][1]==board[2][2]==mark: return True
            if board[0][2]==board[1][1]==board[2][0]==mark: return True
            return False


        _len_o = 0
        _len_x = 0  
        for i in range(len(board)):
            board[i] = list(board[i])
            for j in board[i]:
                if j == "O":
                    _len_o += 1
                elif j == "X":
                    _len_x += 1
        print(_len_o,_len_x)
        if _len_o!=_len_x and _len_x-_len_o!=1:
            return False
        if _len_o==_len_x and check("X"):
            return False
        if _len_o==_len_x-1 and check("O"):
            return False
        return True


if __name__=="__main__":
    board = ["XOX","O O","XOX"]
    a = Solution()
    print(a.validTicTacToe(board))