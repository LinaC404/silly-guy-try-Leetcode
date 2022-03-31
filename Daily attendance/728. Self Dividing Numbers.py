class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        """
        Runtime: 118 ms
        Memory Usage: 14 MB
        """
        res = []
        for i in range(left,right+1):
            nums = str(i)
            for j in range(len(nums)):
                if int(nums[j])==0 or i%int(nums[j])!=0:
                    break
                if j==len(nums)-1:
                    res.append(i)
        return res
     
                    