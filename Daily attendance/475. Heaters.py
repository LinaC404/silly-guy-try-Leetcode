class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        find the radious -> the minimum distance between house and heater
        Runtime: 208 ms, faster than 100.00% of Python online submissions for Heaters.
        Memory Usage: 15.9 MB, less than 68.18% of Python online submissions for Heaters.
        """
        res = 0
        index = 0
        # *
        heaters.append(float("-inf"))
        heaters.append(float("inf"))
        houses.sort()
        heaters.sort()
        for i in range(len(houses)):
            while heaters[index]<houses[i]:
                index += 1 
            temp = min(heaters[index]-houses[i],houses[i]-heaters[index-1])
            res = max(res,temp)
        return res   
        
if __name__=="__main__":
    houses = [1,5]
    heaters = [2]
    a = Solution()
    a.findRadius(houses,heaters)