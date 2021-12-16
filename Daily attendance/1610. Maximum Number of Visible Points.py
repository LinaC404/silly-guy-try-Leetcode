import math 
class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        坐标体系的转换
        环形滑动窗口
        https://zxi.mytechroad.com/blog/sliding-window/leetcode-1610-maximum-number-of-visible-points/
        """
        # transform the coordinate system. location -> original point
        left = right = res =0
        PI = math.pi
        origin_points = 0
        angle_list = []
        for p in points:
            if (p[0]==location[0] and p[1]==location[1]):
                origin_points += 1
                continue
                # compute the angle of each point
                # atan2 (atan: [-PI/2,PI/2])
            angle_list.append(math.atan2(p[1]-location[1],p[0]-location[0]))

        angle_list.sort()
        # slide window -> double it to avoid proble like 315 and 45
        angle_list.extend([i + 2.0*PI for i in angle_list])
        # print(angle_list)

        # right-> , if (angle[r]-angle[l]) > angle ,left->
        # do not forget the points which have the same coordinate!
        angle = math.radians(angle)
        for right in range(len(angle_list)):
            while (angle_list[right]-angle_list[left]>angle):
                left +=1
            res = max(res,right-left+1)
        return res+origin_points


        




            





        
if __name__=="__main__":
    points = [[2,1],[2,2],[3,3]]
    angle = 90
    location = [1,1]
    a = Solution()
    a.visiblePoints(points, angle, location)