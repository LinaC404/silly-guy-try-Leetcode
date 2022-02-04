from collections import defaultdict
class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        Runtime: 144 ms, faster than 94.12% of Python online submissions for Number Of Rectangles That Can Form The Largest Square.
        Memory Usage: 14.1 MB, less than 67.06% of Python online submissions for Number Of Rectangles That Can Form The Largest Square.
        """
        mydict = defaultdict(int)
        for rect in rectangles:
            mydict[min(rect[0],rect[1])] += 1
        return mydict[max(mydict,key=int)]

        
if __name__=="__main__":
    rectangles =[[5,8],[3,9],[3,12]]
    a = Solution()
    print(a.countGoodRectangles(rectangles))