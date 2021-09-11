class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0

        flag = []
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                flag.append(1)
            elif nums[i+1] == nums[i]:
                flag.append(0)
            else:
                flag.append(-1)
        # print(flag)
        
        length = 1
        maxlength = 1 
        j = 0 

        while j < len(flag):
            # print(j)
            if flag[j] == 1:
                for m in range(j,len(flag)):
                    if flag[m]==1:
                        length = length + 1
                    else:
                        break
                if length>maxlength:
                    maxlength = length
                j=m
                
            length = 1
            j = j+1
        print(maxlength)
        return maxlength


if __name__ == '__main__':
    a = Solution()
    nums = []
    result =a.findLengthOfLCIS(nums)
    print(result)