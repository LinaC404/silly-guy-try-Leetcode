class Solution(object):
    def minCostClimbingStairs1(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        Runtime: 54 ms, faster than 60.14% of Python online submissions for Min Cost Climbing Stairs.
        Memory Usage: 13.6 MB, less than 60.79% of Python online submissions for Min Cost Climbing Stairs.
        """
        cost_d = [float('inf') for i in range(len(cost)+2)]
        cost_d[0] = 0
        cost_d[1] = 0
        for i in range(len(cost)):
            cost_d[i+1] = min(cost_d[i+1],cost_d[i]+cost[i])
            cost_d[i+2] = min(cost_d[i+2],cost_d[i]+cost[i])
        return cost_d[-2]
        
    def minCostClimbingStairs2(self, cost):
        dp=[0]*len(cost)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,len(cost)):
            dp[i]=min(dp[i-1],dp[i-2])+cost[i]
        return min(dp[-2:])