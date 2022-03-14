from collections import defaultdict
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        Runtime: 210 ms, faster than 66.82% of Python3 online submissions for Minimum Index Sum of Two Lists.
        Memory Usage: 14.7 MB, less than 24.56% of Python3 online submissions for Minimum Index Sum of Two Lists.
        """
        res = ''
        flag = float('inf')
        my_dict = defaultdict(list)
        for i,v in enumerate(list1):
            my_dict[v].append(i)
        for j,v in enumerate(list2):
            my_dict[v].append(j)
        for m in my_dict:
            if len(my_dict[m]) == 2:
                if sum(my_dict[m])<flag:
                    flag = sum(my_dict[m])
                    res = [m]
                elif sum(my_dict[m])==flag:
                    res.append(m)
        return res

if __name__=="__main__":
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
    a = Solution()
    print(a.findRestaurant(list1,list2))