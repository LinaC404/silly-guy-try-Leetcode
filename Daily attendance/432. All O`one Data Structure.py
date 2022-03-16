from collections import defaultdict
class AllOne(object):

    def __init__(self):
        self.word_dict = defaultdict(int)
        self.word_count = {}

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        Runtime: 333 ms, faster than 39.90% of Python3 online submissions for All O`one Data Structure.
        Memory Usage: 29.6 MB, less than 97.20% of Python3 online submissions for All O`one Data Structure.
        """
        self.word_dict[key] += 1
        count =  self.word_dict[key]
        if count==1:
            if count in self.word_count:
                self.word_count[1].append(key)
            else:
                self.word_count[1] = [key]
        else:
            self.word_count[count-1].remove(key)
            if len(self.word_count[count-1])==0:
                del self.word_count[count-1]
            if count in self.word_count:
                self.word_count[count].append(key)
            else:
                self.word_count[count] = [key]
        # Damn python version
        self.word_count= dict(sorted(self.word_count.items()))
        # print("ADD",key)
        # print("1",self.word_dict)
        # print("2",self.word_count)

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        self.word_dict[key] -= 1
        count =  self.word_dict[key]
        if count==0:
            del self.word_dict[key]
            self.word_count[1].remove(key)
            # if len(self.word_count[1])==0:
            #     del self.word_count[1]

        else:
            self.word_count[count+1].remove(key)
            if count in self.word_count:
                self.word_count[count].append(key)
            else:
                self.word_count[count] = [key]
        if len(self.word_count[count+1])==0:
            del self.word_count[count+1]

        self.word_count= dict(sorted(self.word_count.items()))
        # print("DEL",key)
        # print("3",self.word_dict)
        # print("4",self.word_count)

        

    def getMaxKey(self):
        """
        :rtype: str
        """
        if len(self.word_dict)==0: return ""
        return list(self.word_count.items())[-1][1][0]
        

    def getMinKey(self):
        """
        :rtype: str
        """
        if len(self.word_dict)==0: return ""
        return list(self.word_count.items())[0][1][0]