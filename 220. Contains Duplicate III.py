class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums)==0 or k==0:
            return False
        if  t==0 and len(nums)==len(set(nums)):
            return False

        buckets = {}
        # the index of bucket
        for i in range(0,len(nums)):
            buc_index = int(nums[i]/(t+1))
            print(buc_index)
            if buc_index in buckets:
                return True
            if buc_index-1 in buckets:
                if abs(buckets[buc_index-1]-nums[i])<=t:
                    return True
            if buc_index+1 in buckets:
                if abs(buckets[buc_index+1]-nums[i])<=t:
                    return True
            # Do not forget to delete the bucket 
            # when the range is bigger than k
            if i >= k:
                del buckets[int(nums[i-k]/(t+1))]
            buckets[buc_index] = nums[i]
            print(buckets)
        return False
                




if __name__=="__main__":
    a = Solution()
    nums = [1,5,9,1,5,9]
    k = 2
    t = 3
    a.containsNearbyAlmostDuplicate(nums,k,t) 