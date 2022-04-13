import random
class RandomizedSet(object):
    """
    Runtime: 535 ms, faster than 68.71% of Python online submissions for Insert Delete GetRandom O(1).
    Memory Usage: 58.6 MB, less than 95.35% of Python online submissions for Insert Delete GetRandom O(1).
    """

    def __init__(self):
        self.num_dict = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.num_dict:
            return False
        self.num_dict[val]=1
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.num_dict:
            del self.num_dict[val]
            return True
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(list(self.num_dict))
        
# ---------------------------------------------------------------


class RandomizedSet(object):
    """
    Runtime: 352 ms, faster than 100.00% of Python online submissions for Insert Delete GetRandom O(1).
    Memory Usage: 58.7 MB, less than 83.56% of Python online submissions for Insert Delete GetRandom O(1).
    """

    def __init__(self):
        self.list = []
        self.dic = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        # val: the index in list
        self.dic[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # In list, remove -> O(N)
        # Swap the delete val and the last val, pop it
        if val not in self.dic:
            return False
        last, idx = self.list[-1], self.dic[val]
        self.list[idx],self.dic[last]= last, idx
        del self.dic[val]
        del self.list[-1]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list)