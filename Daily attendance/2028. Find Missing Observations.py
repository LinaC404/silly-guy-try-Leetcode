import math
class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        Runtime: 1628 ms, faster than 89.13% of Python3 online submissions for Find Missing Observations.
        Memory Usage: 23.7 MB, less than 79.35% of Python3 online submissions for Find Missing Observations.
        """
        m = len(rolls)
        goal = mean*(m+n)-sum(rolls)
        res = []
        print(goal)

        if goal/n>6 or goal/n<1: return res
        if goal%n == 0: return [int(goal/n) for i in range(n)]
        else:
            temp = math.ceil(goal/n)
            res = [temp for i in range(n)]
            diff = temp*n-goal
            print(res,diff)
            if diff <= temp-1:
                res[-1] = temp-diff
            else:
                i = 0
                while diff>0:
                    if diff < temp-1:
                        res[i] = temp-diff
                        break
                    diff -= temp-1
                    res[i] = 1
                    i += 1
            return res



        # TLE
        # def dfs(curr):
        #     print(curr,n)
        #     if len(curr) == n and sum(curr)==self.goal:
        #         self.res = curr
        #         return
        #     if sum(curr)>self.goal or len(curr)>n:
        #         print(">>>>")
        #         return
        #     candidates = [1,2,3,4,5,6]
        #     for i in candidates:
        #         dfs(curr+[i])

        # dfs([])
        # print(self.goal)
        # print(self.res)
        
if __name__=="__main__":
    rolls = [1,5,6]
    mean = 3
    n = 4
    a = Solution()
    print(a.missingRolls(rolls, mean, n))
