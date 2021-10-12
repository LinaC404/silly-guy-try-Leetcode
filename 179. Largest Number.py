import functools

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if list(set(nums)) == [0]:
            return '0'
        res = ''
        for i in range(0,len(nums)):
            nums[i] = str(nums[i])
        nums.sort(reverse=True, key=functools.cmp_to_key(lambda x,y: 1 if int(x+y)>int(y+x) else -1))
        res = res.join(nums)
        return res


if __name__ == "__main__":    
    a = Solution()
    a.largestNumber([3,30,34,5,9])