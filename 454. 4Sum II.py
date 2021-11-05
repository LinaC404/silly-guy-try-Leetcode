from collections import defaultdict
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        res = 0
        sum_dict = defaultdict(int)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                temp = nums1[i]+nums2[j]
                sum_dict[temp] = sum_dict[temp]+1
        print(sum_dict)
        for m in range(len(nums3)):
            for n in range(len(nums4)):
                find = 0-(nums3[m]+nums4[n])
                if find in sum_dict:
                    if sum_dict[find]>0:
                        res = res + sum_dict[find]
                        print(nums3[m],nums4[n])
                        print(sum_dict)
        return res

if __name__=="__main__":
    nums1 = [-1,-1]
    nums2 = [-1,1]
    nums3 = [-1,1]
    nums4 = [1,-1]
    a = Solution()
    print(a.fourSumCount(nums1, nums2, nums3, nums4))