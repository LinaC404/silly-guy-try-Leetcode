class Trie(object):

    def __init__(self):
        self.trie = []
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.trie.append(word)


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word in self.trie:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        prefix_len = len(prefix)
        for i in self.trie:
            if i[0:prefix_len] == prefix:
                return True
        return False


        


# Your Trie object will be instantiated and called as such:
if __name__=="__main__":
    trie = Trie()
    print(trie.insert("apple"))
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))  