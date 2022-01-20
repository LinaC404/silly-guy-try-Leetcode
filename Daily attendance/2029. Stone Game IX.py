class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        https://www.youtube.com/watch?v=8MTch2zTOoY&ab_channel=HuifengGuan
        Runtime: 3402 ms, faster than 6.25% of Python online submissions for Stone Game IX.
        Memory Usage: 117.1 MB, less than 6.25% of Python online submissions for Stone Game IX.
        """
        def win(temp,sum,turn):
            print(temp,sum,turn)
            if (temp[0]+temp[1]+temp[2])==0:
                if turn == 1:
                    return True
                else: return False

            if temp[0]>0:
                temp[0] -= 1
                return 1-win(temp,sum,1-turn)
            elif sum%3==1:
                if temp[1]>0:
                    temp[1] -= 1
                    return 1-win(temp,sum+1,1-turn)
                else:
                    return False
            else: #sum%3==2
                if temp[2]>0:
                    temp[2] -= 1
                    return 1-win(temp,sum+2,1-turn)
                else: return False


        count = [0,0,0]
        for s in stones:
            count[s%3] += 1
        # 0 Alice turn
        # 1 Bob   turn
        temp = count[:]
        if temp[1]>0:
            temp[1] -= 1
            # if rival wins, choose this strategy, Alice is not certain to lose
            # if rival loses, go this way
            if win(temp,1,1) == 0:
                return True

        temp = count[:]
        if temp[2]>0:
            temp[2] -= 1
            # a = win(temp,2,1)
            # print(a)
            if win(temp,2,1) == 0:
                return True

        return False
        
        
if __name__=="__main__":
    stones = [20,3,20,17,2,12,15,17,4]
    a = Solution()
    print(a.stoneGameIX(stones))