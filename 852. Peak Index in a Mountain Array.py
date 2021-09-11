class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        peak = max(A)
        result = [i for i in range(len(A)) if A[i]==peak]
        return result[0]
        

if __name__ == "__main__":
    A = [0,2,1,0]
    a = Solution()
    a.peakIndexInMountainArray(A)