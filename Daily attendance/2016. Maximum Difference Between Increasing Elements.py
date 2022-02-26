class Solution(object):
    def mymaximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 37 ms, faster than 66.94% of Python online submissions for Maximum Difference Between Increasing Elements.
        Memory Usage: 13.6 MB, less than 47.52% of Python online submissions for Maximum Difference Between Increasing Elements.
        """
        res = -1
        stack = []
        stack.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]>stack[-1]:
                stack.append(nums[i])              
            else:
                while stack and stack[-1]>=nums[i]:
                    stack.pop()
                stack.append(nums[i])
            if len(stack)>=2: res = max(stack[-1]-stack[0],res)   
        return res
    def maximumDifference(self, nums):
        """
        i find the current smallest num
        j traverse
        => max diff
        """
        i = 0
        j = 1
        max_diff = -1
        while j<len(nums):
            
            if(nums[i]<nums[j]):
                max_diff = max(nums[j]-nums[i], max_diff)
            else:
                i = j
            j = j+1         
        return max_diff
 
        
if __name__ == "__main__":
    nums =[999,997,980,976,948,940,938,928,924,917,907,907,881,878,864,862,859,857,848,840,824,824,824,805,802,798,788,777,775,766,755,748,735,732,727,705,700,697,693,679,676,644,634,624,599,596,588,583,562,558,553,539,537,536,509,491,485,483,454,449,438,425,403,368,345,327,287,285,270,263,255,248,235,234,224,221,201,189,187,183,179,168,155,153,150,144,107,102,102,87,80,57,55,49,48,45,26,26,23,15]
    a = Solution()
    print(a.maximumDifference(nums))