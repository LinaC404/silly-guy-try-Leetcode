class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Not finished 
        """
        res = [0 for i in range(len(nums))]

        def count(i):
            flag = float("inf")
            for j in range(len(nums)-1,i,-1):
                if nums[i]>nums[j]:
                    if nums[j] < flag:
                        flag = nums[j]
                        res[i] = res[i]+1
                    else:
                        res[i] = max(res[i],res[j]+1)


        for i in range(len(nums)-2,-1,-1):
            count(i)
        return res
        
if __name__=="__main__":
    nums = [2,0,1]
    a = Solution()
    print(a.countSmaller(nums))