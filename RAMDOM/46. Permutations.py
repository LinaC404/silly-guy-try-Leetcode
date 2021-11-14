# class Solution(object):
 
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         def recru(res,n,nums):
#             if len(nums) == 0:
#                 print("add",list(n))
#                 res.append(list(n))
#                 return res
#             for i in range(len(nums)):
#                 n.append(nums[i])
#                 num = nums[:i]+nums[i+1:]
#                 print(n,num)
#                 recru(res,n,nums[:i]+nums[i+1:])
#                 print("pop",n[-1],end='')
#                 n.pop()
#                 print(' ',n)


#         res = []
#         recru(res,[],nums)
#         return res

import itertools

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def dfs(head, tail):
            print("head",head,"tail",tail)
            if len(head) == len_:
                print("add",head)
                ans.append(head)
            else:
                for i in range(len(tail)):
                    print(head + [tail[i]], tail[:i] + tail[i+1:])
                    dfs(head + [tail[i]], tail[:i] + tail[i+1:])
        
        len_ = len(nums)
        ans = []
        dfs([], nums)
        return ans
if __name__ == "__main__":
    nums = [1,2,3]
    a = Solution()
    print(a.permute(nums))