class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        Runtime: 3839 ms, faster than 23.91% of Python online submissions for Matchsticks to Square.
        Memory Usage: 13.5 MB, less than 60.87% of Python online submissions for Matchsticks to Square.
        """
        if not matchsticks or len(matchsticks)<4: return False
        div,mod = divmod(sum(matchsticks),4)
        if mod!=0 or max(matchsticks)>div: return False

        matchsticks = sorted(matchsticks,reverse=True)
        target = [div]*4

        def dfs(index,target):
            if index==len(matchsticks):return True
            stick = matchsticks[index]
            for i in range(4):
                if target[i]>= stick:
                    target[i] -= stick
                    if dfs(index+1,target):
                        # all the sticks can be used
                        return True
                    # backtracking, this stick will be used in the next edge
                    target[i] += stick
            return False

        return dfs(0,target)


                



        
if __name__=="__main__":
    matchsticks = [1,2,3,4,5,6,7,8,9,10,5,4,3,2,1]
    a = Solution()
    print(a.makesquare(matchsticks))