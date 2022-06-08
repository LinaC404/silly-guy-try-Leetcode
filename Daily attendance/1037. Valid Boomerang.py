class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        """
        Runtime: 33 ms, faster than 92.40% of Python3 online submissions for Valid Boomerang.
        Memory Usage: 13.9 MB, less than 62.99% of Python3 online submissions for Valid Boomerang.
        """
        points = sorted(points)
        points_set = set()

        for p in points:
            points_set.add((p[0],p[1]))

        slope1 = (points[1][1]-points[0][1])/(points[1][0]-points[0][0]) if points[1][0]!=points[0][0] else float("inf")
        slope2 = (points[2][1]-points[1][1])/(points[2][0]-points[1][0]) if points[2][0]!=points[1][0] else float("inf")
        if len(points_set)!= len(points) or slope1==slope2: return False
        return True

    def isBoomerang2(self, points: List[List[int]]) -> bool:
        return (points[0][0] - points[1][0]) * (points[1][1] - points[2][1]) != (points[1][0] - points[2][0]) * (points[0][1] - points[1][1])

if __name__=="__main__":
    a = Solution()
    print(a.isBoomerang(points = [[52,86],[12,65],[24,71]]))