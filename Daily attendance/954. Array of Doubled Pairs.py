from collections import Counter
class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        https://maxming0.github.io/2021/08/11/Array-of-Doubled-Pairs/
        Runtime: 584 ms, faster than 98.50% of Python3 online submissions for Array of Doubled Pairs.
        Memory Usage: 16.6 MB, less than 39.35% of Python3 online submissions for Array of Doubled Pairs.
        """
        # a 2a b 2b ...
        count = Counter(arr)
        for i in sorted(count,key=abs):
            if count[i] > count[2*i]:
                return False
            count[2*i] -= count[i]
        return True


        
        
   






if __name__=="__main__":
    arr = [4,-2,2,-4]
    a = Solution()
    print(a.canReorderDoubled(arr))