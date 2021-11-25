import math
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        http://potatomatooo.blogspot.com/2020/11/leetcode-458-poor-pigs-python.html
        e.g 
        1 pig minutesToDie=15 minutesToTest=60
        pig1 1  2  3  4  5   can test 5 bucket

        pig1&pig2
        1   2   3   4   5
        6   7   8   9   10
        11  12  13  14  15
        16  17  18  19  20
        21  22  23  24  25
        
        pig 1 drinks a row while pig2 drink a column
        if pig 1 die at minute 60-> [16,17,18,19,20] has posion
            if pig 2 die at minute 15 ->tag 16 
            if pig 2 alive -> tag 20
        all alive -> tag 25
        .
        .
        .
        n pigs ->(minutesToTest/minutesToTest+1)^n>=the number of bucket
        """
        temp = int(minutesToTest/minutesToDie)+1
        return math.ceil(math.log(buckets,temp))

if __name__=="__main__":
    buckets = 1000
    minutesToDie = 15
    minutesToTest = 60
    a = Solution()
    a.poorPigs(buckets,minutesToDie,minutesToTest)