class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        step = 0
        curr_cap = capacity
        plants.insert(0,-1)
        # print(plants)
        for i in range(1,len(plants)):
            if curr_cap < plants[i]:
                print(i)
                curr_cap = capacity
                step  = step+i-1+i
                curr_cap = curr_cap-plants[i]
            else:
                curr_cap = curr_cap-plants[i]
                step = step+1
        return step
        
            # print("step",step)
            # print("curr_cap",curr_cap)

            

if __name__=="__main__":
    plants = [7,7,7,7,7,7,7]
    capacity = 8
    a = Solution()
    a.wateringPlants(plants,capacity)