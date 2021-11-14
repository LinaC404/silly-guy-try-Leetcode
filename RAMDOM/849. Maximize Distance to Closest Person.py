import math

class Solution(object):

    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        seated = [i for i in range(len(seats)) if seats[i]==1]
        print(seated)
        flag = 1
        if seated[0] != 0:
            flag = seated[0]

        for i in range(len(seated)-1):
            mm = seated[i+1]-seated[i]
            mm = math.floor(mm/2)
            if mm>flag:
                flag = mm

        if seated[-1]!= len(seats)-1:
            mm = len(seats)-1-seated[-1]
            if mm>flag:
                flag = mm
        return int(flag)





        

if __name__ == "__main__":
    seats = [1,0,0,0]
    a = Solution()
    print(a.maxDistToClosest(seats))