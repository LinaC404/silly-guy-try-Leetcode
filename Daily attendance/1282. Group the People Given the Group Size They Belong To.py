from collections import defaultdict
class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        Runtime: 69 ms, faster than 71.83% of Python online submissions for Group the People Given the Group Size They Belong To.
        Memory Usage: 13.8 MB, less than 10.56% of Python online submissions for Group the People Given the Group Size They Belong To.
        """
        ans = []
        groupdict = defaultdict(list)
        for i,size in enumerate(groupSizes):
            groupdict[size].append(i)
        
        for size,indexs in groupdict.items():
            for i in range(0,len(indexs),size):
                ans.append(indexs[i:i+size])       
        return ans