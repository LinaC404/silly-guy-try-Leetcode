class MySolution(object):
    def longestSubarray(self, nums, limit):
        """
        Time Limit Exceeded
        55 / 61 test cases passed.
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        if len(nums)==1: return 1

        ans = 0
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for i in range(len(nums)):
            dp [i][i]=[8,8]
            curmax = nums[i]
            curmin = nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]>=curmax:
                    curmax = nums[j]
                if nums[j]<=curmin:
                    curmin = nums[j]
                if abs(curmax-curmin)<=limit:
                    if j-i+1>ans:
                        ans = j-i+1
        return ans

from collections import deque

class Solution(object):
    """
    https://www.youtube.com/watch?v=p8-f0_CwWLk
    binary tree      N^2 -> NlogN

    Monoyonic Queue  N^2 -> N
    最小值 单调递增
    最大值 单调递减
    
    
    对collcetions中的内置数据结构的操作不熟悉
    """
    def longestSubarray(self, nums, limit):
        max_queue = deque()
        min_queue = deque()
        ans = 0
        left = 0
        for right in range(len(nums)):
            while max_queue and nums[right]>max_queue[-1]:
                max_queue.pop()
            while min_queue and nums[right]<min_queue[-1]:
                min_queue.pop()
            max_queue.append(nums[right])
            min_queue.append(nums[right])

            while(max_queue[0]-min_queue[0]>limit):
                # 除去要删除元素
                if nums[left]==min_queue[0]:
                    min_queue.popleft()
                if nums[left]==max_queue[0]:
                    max_queue.popleft()
                left = left+1

            ans = max(ans,right-left+1)
        return ans
             
        


if __name__=="__main__":
    nums = [8,2,4,7]
    limit = 4
    a = Solution()
    print(a.longestSubarray(nums,limit))
