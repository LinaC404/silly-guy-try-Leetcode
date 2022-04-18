class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        Runtime: 68 ms, faster than 97.31% of Python online submissions for Trapping Rain Water.
        Memory Usage: 15.2 MB, less than 27.09% of Python online submissions for Trapping Rain Water.
        """
        res = 0
        l,r = [0 for i in range(len(height))],[0 for i in range(len(height))]
        l[0] = height[0]
        r[-1] = height[-1]
        for i in range(1,len(height)):
            l[i] = max(l[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            r[i] = max(r[i+1],height[i])
        for i in range(len(height)):
            res+= min(l[i],r[i])-height[i]
        return res
# ---------------------------------------------------- Two pointer

                    
if __name__=="__main__":
    a = Solution()
    print(a.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))