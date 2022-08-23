from collections import Counter
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=s67anzv0rGM&ab_channel=HappyCoding
        1. check if the chessboard is vaild
            1> only two type of rows/cols
            2> rows/cols should be complementary
            3> the count value of types should be same or the diff is 1
            4> in each line, the number of 0/1 should be same or diff is 1
        2. rows moves + cols moves
        Runtime: 135 ms, faster than 37.93% of Python3 online submissions for Transform to Chessboard.
        Memory Usage: 14 MB, less than 58.62% of Python3 online submissions for Transform to Chessboard.
        """
        n = len(board)
        ans = 0

        rowCnt = Counter(map(tuple,board))
        colCnt =Counter(zip(*board))
        for count in (rowCnt,colCnt):
            # case 1
            if len(count)!=2:
                return -1
            # case 2
            # 0 1 1 0  --
            #            | x^y==1
            # 1 0 0 1  --
            l1,l2 = count
            if not all(i^j for i, j in zip(l1,l2)):
                return -1
            # case 3
            if sorted(count.values())!=[n//2,(n+1)//2]:
                return -1
            # case 4
            for line in count:
                line_count = Counter(line)
                if sorted(line_count.values())!=[n//2,(n+1)//2]:
                    return -1
            
            if n%2:
                max_line = count.most_common(1)[0][0]
                tar = 1 if max_line.count(1)>max_line.count(0) else 0
                moves = 0
                for x in max_line:
                    moves += x^tar
                    tar ^= 1
                # do not forget to //2, because the once swaped, the next row/col do not need to swap
                ans += moves//2
            else:
                # set the start as 0 or 1, get the minimum steps
                moves = float("inf")
                for tar in (0,1):
                    temp = 0
                    for x in l1:
                        temp += x^tar
                        tar ^= 1
                    moves = min(moves,temp//2)
                ans += moves
        return ans


if __name__=="__main__":
    a = Solution()
    print(a.movesToChessboard(board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]))
        