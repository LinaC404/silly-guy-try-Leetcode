from collections import defaultdict
class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 604 ms, faster than 75.00% of Python online submissions for Maximum Equal Frequency.
        Memory Usage: 19.8 MB, less than 16.67% of Python online submissions for Maximum Equal Frequency.
        """
        num_fre = defaultdict(int)
        fre_count = defaultdict(int)

        for n in nums:
            num_fre[n] += 1
            fre_count[num_fre[n]] += 1

        
        for i in range(len(nums)-1,0,-1):
            # remove previous one        
            if num_fre[nums[i]]*fre_count[num_fre[nums[i]]]==i:
                return i+1
            else:
                # remove current one
                fre_count[num_fre[nums[i]]] -= 1
                num_fre[nums[i]] -= 1
                # fre_count[num_fre[nums[i]]] += 1
                if num_fre[nums[i-1]]*fre_count[num_fre[nums[i-1]]]==i:
                    print(">>",i-1,nums[i-1])
                    return i+1
        return 1

        

if __name__=="__main__":
    a = Solution()
    print(a.maxEqualFreq([1]))