from collections import Counter,defaultdict
class Solution(object):
    def mydeleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 92 ms, faster than 25.39% of Python online submissions for Delete and Earn.
        Memory Usage: 15.7 MB, less than 9.69% of Python online submissions for Delete and Earn.
        """
        num_count = Counter(nums)
        num_list = sorted(set(nums))
        if len(nums)==1: return num_list[0]*num_count[num_list[0]]
        dp = [0 for i in range(len(num_list))]
        dp[0] = num_list[0]*num_count[num_list[0]]
        dp[1] = max(num_list[1]*num_count[num_list[1]],dp[0]) if num_list[1]-num_list[0]==1 else num_list[1]*num_count[num_list[1]]+dp[0]

        for i in range(2,len(num_list)):
            if num_list[i]-1 == num_list[i-1]:
                temp = num_list[i]*num_count[num_list[i]]+dp[i-2]
                dp[i] = max(dp[i-1],temp)
            else:
                dp[i] = dp[i-1]+num_list[i]*num_count[num_list[i]]
        return dp[-1]
    # -----------------------------------------------------------
    def deleteAndEarn(self, nums):
        """
        Runtime: 140 ms, faster than 12.73% of Python online submissions for Delete and Earn.
        Memory Usage: 15.2 MB, less than 15.08% of Python online submissions for Delete and Earn.
        """
        points = defaultdict(int)
        for num in nums:
            points[num] += num
        # get points of same digit
        max_num = max(points)
        
        # Avoid KeyError, start with 1
        max_points = defaultdict(int)
        max_points[1] = points[1]
       
        for num in range(2, max_num+1):
            max_points[num] = max(max_points[num-1], max_points[num-2] + points[num])
        
        return max_points[max_num]

        
if __name__=="__main__":
    nums = [2,4,5,5,5,6]
    a = Solution()
    print(a.deleteAndEarn(nums))