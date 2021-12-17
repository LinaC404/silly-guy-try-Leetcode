class Solution(object):
    def mynumWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        Runtime: 29 ms
`       Memory Usage: 13.6 MB
        """
        self.res = numBottles
        def change(bottles):
            if bottles<numExchange:
                return
            newbottle = int(bottles/numExchange)
            remain = bottles-newbottle*numExchange
            self.res = self.res+newbottle
            change(newbottle+remain)

        change(numBottles)
        return self.res

    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        return int(numBottles + (numBottles - 1) / (numExchange - 1))
        

if __name__ =="__main__":
    numBottles = 9
    numExchange = 3
    a = Solution()
    a.numWaterBottles(numBottles,numExchange)