class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left,right = 0, len(arr)-1
        res = -1
        while left <= right:
            i = (left + right) // 2
            if arr[i]>arr[i+1]:
                res = i
                right = i -1
            else:
                left = i + 1
        return res

        
if __name__ == "__main__":
    arr = [3,10,9,7,4]
    a = Solution()
    print(a.peakIndexInMountainArray(arr))
