class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        https://www.youtube.com/watch?v=XSxnbDFz_2U&ab_channel=HuifengGuan
        two properties -> fix one property
        Monotone Stack 
        What is weak
        [1  2  2  3  4  5  6]
        [3] <- 4               pop 3 
        [4]  <- 1
        [4  1]
        [4  1] <- 6
        [6]                    pop 4 1
        ....
        Runtime: 4255 ms, faster than 8.11% of Python online submissions for The Number of Weak Characters in the Game.
        Memory Usage: 69.4 MB, less than 79.73% of Python online submissions for The Number of Weak Characters in the Game.
        """

        # https://stackoverflow.com/questions/62208185/what-does-arr-sortkey-lambda-x-x0-x1-mean/62208276#62208276
        #  this generates tuples of (the first element, negative of the second element)
        #  1. The first element
        #  2. If the first elements are equal, then the second element

        properties = sorted(properties, key=lambda x:(x[0],-x[1]))
        print(properties)
        defence = []
        defence.append(properties[0])
        res = 0

        for i in range(1,len(properties)):
            while defence:
                if properties[i][1]>defence[-1][1]:
                    defence.pop()
                    res += 1
                else:
                    break
            defence.append(properties[i])
        return res
        
if __name__=="__main__":
    properties = [[1,5],[10,4],[4,3]]
    a = Solution()
    print(a.numberOfWeakCharacters(properties))