from collections import defaultdict
class MagicDictionary(object):

    def __init__(self):
        self.dict = defaultdict(list)
        

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        Runtime: 98 ms, faster than 90.38% of Python online submissions for Implement Magic Dictionary.
        Memory Usage: 13.9 MB, less than 86.54% of Python online submissions for Implement Magic Dictionary.
        """
        for word in dictionary:
            _len = len(word)
            self.dict[_len].append(word)
        # print(self.dict)
            
        

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        _tar = len(searchWord)
        if _tar not in self.dict: return False
        for word in self.dict[_tar]:
            diff = 0
            if word == searchWord:
                continue
            for i in range(_tar):
                if word[i]!=searchWord[i]:
                    diff += 1
                    if diff>1: break
            if diff == 1:
                return True    
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
if __name__=="__main__": 
    dictionary = ["hello", "leetcode"]
    obj = MagicDictionary()
    obj.buildDict(dictionary)
    print(obj.search("bb"))
    print(obj.search("hhllo"))