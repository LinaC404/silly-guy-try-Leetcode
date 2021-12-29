from collections import defaultdict
class Solution(object):
    def mycountQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Runtime: 192 ms, faster than 80.39% of Python online submissions for Count Special Quadruplets.
`       Memory Usage: 13.3 MB, less than 74.51% of Python online submissions for Count Special Quadruplets.
        """
        res = 0

        age_dict = defaultdict(list)
        for i,age in enumerate(nums):
            age_dict[age].append(i)
        
        for a in range(len(nums)-3):
            for b in range(a+1,len(nums)-2):
                for c in range(b+1,len(nums)-1):
                    total = nums[a]+nums[b]+nums[c] 
                    if total in age_dict:
                        for index in age_dict[total]:
                            if index > c:
                                res += 1
        return res

    def countQuadruplets(self, nums):
        """
        :type nums: List[int]0
        :rtype: int
        Runtime: 40 ms, faster than 100.00% of Python online submissions for Count Special Quadruplets.
        Memory Usage: 13.4 MB, less than 74.51% of Python online submissions for Count Special Quadruplets.
        O(N^3) -> O(N^2)
        1.                        dif(nums[k]-nums[i])   -> map
        2. i <<
        3. if sum(nums[j]+nums[i]) in map                 -> res += 1

          [X X X X X X X X X]     [Y Y Y Y Y Y Y Y Y ]
                           ^  <-                     
                           i
          ---------------- 
                 j                -------------------
                                                   ^    <-
                                                   k
        """
        if len(nums) <= 3:
            return 0 
        else:
            res = 0
            map = {}
            map[nums[-1]-nums[-2]] = 1
            for i in range(len(nums)-3,-1,-1):
                for j in range(i-1,-1,-1):
                    sum_j_i  = nums[i]+nums[j]
                    if sum_j_i in map:
                        res += map[sum_j_i]

       
                
                for k in range(len(nums)-1,i,-1):
                    dif_k_i = nums[k]-nums[i]
                    if  dif_k_i in map:
                        map[dif_k_i] += 1
                    else:
                        map[dif_k_i] = 1
                
            return res 

if __name__=="__main__":
    nums = [1,1,1,3,5]
    a = Solution()
    a.countQuadruplets(nums)