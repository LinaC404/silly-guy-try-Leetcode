class Solution:
    def subArrayRanges(self, nums):
        # Monotone Stack => find the max/min
        # [N1,N2,...,N]               next
        #             [----[pop]-----]   <= min/max
        #  len          a    *   b       * value
        """
        Runtime: 156 ms, faster than 65.12% of Python3 online submissions for Sum of Subarray Ranges.
        Memory Usage: 14.2 MB, less than 30.66% of Python3 online submissions for Sum of Subarray Ranges.
        """
        part_min = 0
        part_max = 0
        
        stack = [(float('-inf'), -1)]
        for i, v in enumerate(nums + [float('-inf')]):
            while stack[-1][0] > v:
                ov, oi = stack.pop()
                part_min += ov * (i - oi) * (oi - stack[-1][1])
            stack.append((v, i))


        stack = [(float('inf'), -1)]
        for i, v in enumerate(nums + [float('inf')]):
            while stack[-1][0] < v:
                ov, oi = stack.pop()
                part_max += ov * (i - oi) * (oi - stack[-1][1])
            stack.append((v, i))
       
        return part_max - part_min

if __name__=="__main__":
    a = Solution()
    print(a.subArrayRanges(nums = [4,-2,-3,4,1]))