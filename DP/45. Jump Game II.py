class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 183 ms, faster than 46.32% of Python online submissions for Jump Game II.
        Memory Usage: 14.4 MB, less than 37.48% of Python online submissions for Jump Game II.
        """
        # o   o   o   o   o   o   o   o   o 
        # curr-----------max_cur
        #        nums[i]
        #         curr ----------------max_cur
        #  BFS  ->  use max_curr to mark the max distance we can reach
        res = curr = max_curr = 0
        for i in range(len(nums)-1):
            max_curr = max(max_curr,i+nums[i])
            print(max_curr)
            if curr == i:
                res += 1
                curr = max_curr
                print("-----",curr)
            print(max_curr)
        return res
 



if  __name__=="__main__":
    nums = [2,1]
    a = Solution()
    print(a.jump(nums))
        