class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 32 ms, faster than 45.45% of Python online submissions for Wiggle Subsequence.
        Memory Usage: 13.3 MB, less than 70.13% of Python online submissions for Wiggle Subsequence.
        """
        df = [0]*len(nums)
        df[0] = 1

        def count(df,mark):
            for i in range(1,len(nums)):
                diff = nums[i] - nums[i-1]
                if diff>0 and mark<0:
                    df[i] = df[i-1]+1
                    mark = 1
                elif diff<0 and mark>0:
                    df[i] = df[i-1]+1
                    mark = -1
                else:
                    df[i] = df[i-1]
            return df

        return max(count(df,1)[-1],count(df,-1)[-1])
        
                

            


        
if __name__=="__main__":
    nums = [1,17,5,10,13,15,10,5,16,8]
    a = Solution()
    print(a.wiggleMaxLength(nums))