class Solution(object):
    def bestRotation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        diff array
        https://www.youtube.com/watch?v=xFlO0H1l2oQ&ab_channel=HuifengGuan
        https://zhuanlan.zhihu.com/p/117569086
        Runtime: 1831 ms, faster than 21.92% of Python3 online submissions for Smallest Rotation with Highest Score.
        Memory Usage: 26.5 MB, less than 100.00% of Python3 online submissions for Smallest Rotation with Highest Score.
        """
        N = len(nums)
        score,ss= 0,0
        res = -1
        diff = [0 for i in range(N)]
        for i in range(N):
            if i>=nums[i]:
                diff[0] += 1
                diff[(i-(nums[i]-1))%N] -= 1
                diff[(i+1)%N] += 1 
            else:
                #  diff[0] += 0
                diff[(i+1)%N] += 1
                # diff[i+1+N-1-(nums[i]-1)] -= 1
                diff[(i+1+N-nums[i])%N] -= 1
        for i,s in enumerate(diff):
            ss += s
            if ss>score:
                score = ss
                res = i
        return res
        
if __name__=="__main__":
    a = Solution()
    print(a.bestRotation([2,3,1,4,0]))