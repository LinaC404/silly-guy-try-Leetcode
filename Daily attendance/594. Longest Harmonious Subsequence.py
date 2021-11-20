from collections import defaultdict,Counter
class Solution(object):
    def findLHS(self, nums):
        """
        Runtime: 361 ms,
        :type nums: List[int]
        :rtype: int
        """
        sum_dict = defaultdict(list)
        for i in range(len(nums)):
            sum_dict[nums[i]].append(i)
        sum_list = sorted(sum_dict.items())
        # print(sum_dict)
        # print(sum_list)
        res = 0
        for j in range(1,len(sum_list)):
            if sum_list[j][0] == sum_list[j-1][0]+1:
                res = max(len(sum_list[j][1])+len(sum_list[j-1][1]),res)
        return res


    def findLHS1(self, nums):
        """
        406ms
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        count = Counter(nums)
        for c in count:
            if c+1 in count:
                res = max(res,count[c]+count[c+1])
        return res
if __name__=="__main__":
    nums = [1,3,2,2,5,2,3,7]
    a = Solution()
    a.findLHS1(nums)