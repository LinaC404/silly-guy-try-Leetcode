class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        https://zxi.mytechroad.com/blog/algorithms/binary-search/leetcode-4-median-of-two-sorted-arrays/
        O(log) -> hint: Binary search
        swap the nums, make sure the len(nums1) is smaller -> reduce time complexity O(log(min(len(nums1),len(nums2))))
        """
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1
        m,n = 0,len(nums1)
        # add one to make it work with both odd and even
        tar = (len(nums1)+len(nums2)+1)/2
        print(nums1,nums2)
        while m<n:
            i = int(m+(n-m)/2)
            j = int(tar - i)
            print(i,j)
            # too far on left side  ---> 
            if nums1[i]<nums2[j-1]:
                m = i + 1
            # too far on right side <---
            else:
                n = i

        i = m
        j = int(tar - i)

        # the left/right side does not have element
        c1 = max(-float('inf') if i<=0 else nums1[i-1], -float('inf') if j<=0 else nums2[j-1])
        c2 = min(float('inf') if i>=len(nums1) else nums1[i], float('inf') if j>=len(nums2) else nums2[j])

        if (len(nums1)+len(nums2))%2 == 1:
            return c1
        else:
            return (c1+c2)*1.0/2

if __name__=="__main__":
    nums1 = [1,2,3,4,5]
    nums2 = [-3,-2,-1]
    a = Solution()
    a.findMedianSortedArrays(nums1,nums2)