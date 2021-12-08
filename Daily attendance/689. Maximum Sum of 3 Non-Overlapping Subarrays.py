from collections import defaultdict
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        抄的，不会 人失了智
        DP： 找到中间数组，左右找最大值，
        ↓可以运用在m个窗口
        https://www.youtube.com/watch?v=r_uJ9Vlqaqs&ab_channel=RenZhang
        """
        # Calculate the sum of all the subarrays (len = k)
        m = 3
        win_sums = [sum(nums[:k])]
        for i in range(1,len(nums)-k+1):
            win_sums.append(win_sums[-1]-nums[i-1]+nums[i-1+k])
        print(win_sums)

        # The defaultdict constructor expects a callable,
        # what we need is a function which returns [the max sum of 1st/2nd ....,[the start index of subarray]]
        # Here i is the index of window, if the (current sum of window + previous max) is bigger
        # update the max_val and index
        # It looks like 
        # [1,2,1,2,6,7,5,1]
        # start_index:0
        # win1   l:0  win_sum:3(1+2)      {0: [0, []], 1: [3, [0]]}
        # win2   l:2  win_sum:3(1+2)      {0: [0, []], 1: [3, [0]], 2: [6, [0, 2]]}
        # win3   l:4  win_sum:13(6+7)     {0: [0, []], 1: [3, [0]], 2: [6, [0, 2]], 3: [19, [0, 2, 4]]})
        # start_index:1
        # win1   l:1  win_sum:3(2+1)      no change
        # win2   l:3  win_sum:8(2+6)      {0: [0, []], 1: [3, [0]], 2: [11, [0, 3]], 3: [19, [0, 2, 4]]})
        # win3   l:5  win_sum:12(7+5)     {0: [0, []], 1: [3, [0]], 2: [11, [0, 3]], 3: [23, [0, 3, 5]]})
        # start_index:2
        # win1   l:2  win_sum:3(1+2)      no change
        # win2   l:4  win_sum:13(6+7)     {0: [0, []], 1: [3, [0]], 2: [16, [0, 4]], 3: [23, [0, 3, 5]]})
        # win3   l:6  win_sum:6(5+1)      no change

        res_dict = defaultdict(lambda: [0,[]])
        
        for start_index in range(len(nums)-k*m+1):
            for i in range(1,m+1):
                l = start_index+(i-1)*k
                win_sum = win_sums[l]
                if win_sum + res_dict[i-1][0] > res_dict[i][0]:
                    res_dict[i][0] = win_sum + res_dict[i-1][0]
                    res_dict[i][1] = res_dict[i-1][1] + [l]
        return res_dict[m][1]



if __name__=="__main__":        
    nums = [1,2,1,2,6,7,5,1]
    k = 2
    a = Solution()
    a.maxSumOfThreeSubarrays(nums,k)