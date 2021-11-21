from collections import defaultdict
from bisect import bisect_left, bisect_right
import copy
"""TLE"""
# class RangeFreqQuery(object):
#     def __init__(self, arr):
#         """
#         :type arr: List[int]
#         """
#         self.arr = arr
#         self.arr_dict = defaultdict(list)
#         for i in range(len(self.arr)):
#             self.arr_dict[self.arr[i]].append(i)
        

#     def query(self, left, right, value):
#         """
#         :type left: int
#         :type right: int
#         :type value: int
#         :rtype: int
#         """
#         if not self.arr_dict[value]: return 0
#         res = 0
#         flag = 0
#         indexs =copy.deepcopy(self.arr_dict[value])
#         if not left in indexs:
#             flag = flag - 1
#             indexs.append(left)
#         if not right in indexs:
#             flag = flag - 1
#             indexs.append(right)
#         indexs.sort()
#         i_left = indexs.index(left)
#         i_right = indexs.index(right)
#         return len(indexs[i_left:i_right+1])+flag
class RangeFreqQuery:
    def __init__(self, arr):
        self.O = O = defaultdict(list)
        for i, a in enumerate(arr):
            O[a].append(i)

        print(self.O)

    def query(self, left: int, right: int, v: int) -> int:
        """
        https://docs.python.org/3/library/bisect.html
        bisect_left/right if x exists return index, else return the insertion index   
        bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
        all(val < x for val in a[lo : i]) for the left side and all(val >= x for val in a[i : hi]) for the right side.

        bisect.bisect(a, x, lo=0, hi=len(a))
        all(val <= x for val in a[lo : i]) for the left side and all(val > x for val in a[i : hi]) for the right side.
        """
        _all = self.O[v]
        l = bisect_left(_all, left)
        r = bisect_right(_all, right)
        
        return r-l


# Your RangeFreqQuery object will be instantiated and called as such:
arr = []
obj = RangeFreqQuery([2,2,1,2,2])
param_1 = obj.query(2, 4, 1)
param_2 = obj.query(1, 3, 1)
param_3 = obj.query(0, 2, 1)