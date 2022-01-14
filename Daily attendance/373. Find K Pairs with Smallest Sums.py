class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        https://github.com/wisdompeak/LeetCode/tree/master/Binary_Search/373.Find-K-Pairs-with-Smallest-Sums

        Step1.  Use binary search to decide the number of x 
                nums1[i]+nums2[j] = x and [[0,0],[...],[i,j]]
                                          __________________ the length is k
        Step2. function count(x)
                                 --> Calculate the number of pairs when sum(nums1[i],nums2[j]) <= x
        Step3. res1=[sum()<x] and res2[sum()==x]   ->  len(res) = k 
        
        Runtime: 2395 ms, faster than 5.24% of Python online submissions for Find K Pairs with Smallest Sums.
        Memory Usage: 73.4 MB, less than 5.24% of Python online submissions for Find K Pairs with Smallest Sums.
        """
        def count(x):
            count_sum = 0
            j = len(nums2)-1
            for i in range(len(nums1)):
                while j>=0 and nums1[i]+nums2[j]>x:
                    j = j - 1
                count_sum = count_sum + j + 1
            return count_sum
            
        # ? Step1. has answer --->  left==right

        left,right = nums1[0]+nums2[0], nums1[-1]+nums2[-1]
        while left<right:
            mid = left + (right-left)//2
            m = count(mid)

            # count(mid) and lessen the range 
            # (convergence and meet the condition)
            # ---> left == right
            if m>=k:  
                right = mid
            else:
                left = mid+1
        
        res1 = []
        res2 = []
        for i in range(len(nums1)):
            j = 0
            while j<len(nums2) and nums1[i]+nums2[j]<=right:
                if nums1[i]+nums2[j]<right:
                    res1.append([nums1[i],nums2[j]])
                else:
                    res2.append([nums1[i],nums2[j]])
                j = j + 1
        nn = len(res1)
        res1.extend(res2[:k-nn])
        return res1



if __name__ == "__main__":
    nums1 = [0,0,0,0,0]
    nums2 = [-3,22,35,56,76]
    k = 22
    a = Solution()
    print(a.kSmallestPairs(nums1,nums2,k))