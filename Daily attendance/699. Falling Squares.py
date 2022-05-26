class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        Runtime: 474 ms, faster than 37.50% of Python online submissions for Falling Squares.
        Memory Usage: 14.1 MB, less than 75.00% of Python online submissions for Falling Squares.
        """
        ans = [0 for i in range(len(positions))]
        # (start,end,height)
        interval = [(positions[0][0],positions[0][0]+positions[0][1],positions[0][1])]
        for i in range(1,len(positions)):
            l,r = positions[i][0],positions[i][0]+positions[i][1]
            h = 0
            for seg in interval:
                if seg[1]<=l or seg[0]>=r:
                    continue
                else:
                    h = max(h,seg[2])
            h += positions[i][1]
            ans[i] = h
            interval.append((positions[i][0],positions[i][0]+positions[i][1],h))
        curr = 0 
        for i,f in enumerate(interval):
            curr = max(curr,f[2])
            ans[i] = curr
        return ans


           


if __name__=="__main__":
    positions = [[1,2],[2,3],[6,1]]
    a = Solution()
    print(a.fallingSquares(positions))
