from bisect import bisect, bisect_right
class Solution(object):
    def myfindClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        Runtime: 321 ms, faster than 72.76% of Python online submissions for Find K Closest Elements.
        Memory Usage: 15.1 MB, less than 44.38% of Python online submissions for Find K Closest Elements.
        """
        ans_len = 0
        idx = bisect_right(arr,x)
        if idx==0: return arr[:k]
        if idx==len(arr): return arr[len(arr)-k:]
        
        l,r = idx-1,idx
        while ans_len<k and l>=0 and r<len(arr):
            if abs(arr[l]-x)<=abs(arr[r]-x):
                ans_len += 1
                l -= 1
                if l==-1:
                    return arr[l+1:r+k-ans_len]
            else:
                ans_len += 1
                r += 1
                if r>=len(arr):
                    return arr[l-k+ans_len+1:r]
        return arr[l+1:r]

    def findClosestElements(self, arr, k, x):
        if x <= arr[0]: 
            return arr[:k]
        if x >= arr[-1]:
            return arr[-k:]

        left = 0
        right = len(arr) - k # max start point
        while left < right:
            mid = left + (right - left) // 2

            # mid + k is closer to x, discard mid by assigning left = mid + 1
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1

            # mid is equal or closer to x than mid + k, remains mid as candidate
            else:
                right = mid

        # left == right, which makes both left and left + k have same diff with x
        return arr[left : left + k]


if __name__=="__main__":
    a = Solution()
    print(a.findClosestElements([1,2,3,4,5,6,7,8,9,10], k = 3, x = 7))