from collections import Counter
class Solution:
    def findDuplicates1(self, nums: List[int]) -> List[int]:
        """
        Runtime: 458 ms
        Memory Usage: 22.8 MB
        """
        count = Counter(nums)
        return [i for i,j in count.items() if j==2]
    def findDuplicates2(self, nums: List[int]) -> List[int]:
        """
        Runtime: 343 ms, faster than 97.16% of Python3 online submissions for Find All Duplicates in an Array.
        Memory Usage: 24.1 MB, less than 5.42% of Python3 online submissions for Find All Duplicates in an Array.
        """
        sett = set()
        lst = []
        for i in nums:
            if i not in sett:
                sett.add(i)
            else:
                lst.append(i)
        return lst