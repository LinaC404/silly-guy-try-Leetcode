import heapq
class Solution(object):
    def mylargestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Runtime: 28 ms, faster than 93.02% of Python online submissions for Maximize Sum Of Array After K Negations.
        Memory Usage: 13.6 MB, less than 41.86% of Python online submissions for Maximize Sum Of Array After K Negations.
        """
        less = [i for i in nums if i<0]
        bigger = [i for i in nums if i>=0]
        res = 0
        less.sort()
        bigger.sort()
        if len(less)>0:
            j = 0
            while k > 0 and j <len(less):
                less[j] = -less[j]
                j = j+1
                k = k-1

        if  k%2==0 or k==0 or (0 in nums):
            res = sum(less)+sum(bigger)
            return res

        if less and bigger:
            if less[-1]<bigger[0]:
                less[-1] = -less[-1]
            else:
                bigger[0] = -bigger[0]
        elif less:
            less[-1] = -less[-1]
        else:
            bigger[0] = -bigger[0]
        res = sum(less)+sum(bigger)

        return res

    def largestSumAfterKNegations(self, nums, k):
        """
        Runtime: 52 ms, faster than 51.00% of Python3 online submissions for Maximize Sum Of Array After K Negations.
        Memory Usage: 14.3 MB, less than 56.57% of Python3 online submissions for Maximize Sum Of Array After K Negations.
        """
        sum_list = sum(nums)
        heapq.heapify(nums)
        while k > 0:
            curr = heapq.heappop(nums)
            k = k -1
            sum_list += 2*(-curr)
            heapq.heappush(nums,-curr)
        return sum_list


        
if __name__=="__main__":
    nums = [-4,-2,-3,0,1]
    k = 10
    a = Solution()
    a.largestSumAfterKNegations(nums,k)
    # a = []
    # print(sum(a))
    # if a:
    #     print("333")