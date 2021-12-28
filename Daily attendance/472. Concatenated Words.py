class Trie(object):
    def __init__(self):
        self.nodes={}
    def insert(self,word):
        curr = self.nodes
        for char in word:
            if not char in curr:
                curr[char] = {}
            curr = curr[char]
        curr['#'] = True

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        我摊牌 我抄的 今天也是借鉴的一天 
        https://www.youtube.com/watch?v=dsnTJscs4BA&ab_channel=HuifengGuan
        Runtime: 1636 ms, faster than 99.39% of Python online submissions for Concatenated Words.
        Memory Usage: 52 MB, less than 43.64% of Python online submissions for Concatenated Words.
        """
        res = []
        root = Trie()
        # sort the array by the length of word
        words.sort(key = lambda x:len(x))

        # word:   XXX       XXXXX
        # j:      matched   ^      is the current index  
        def dfs(word,j,node,visited):
            print(word,j)
            print(visited)
            if j==len(word):
                return True
            
            # Optimization
            if visited[j]==1:
                return False

            for i in range(j,len(word)):
                if word[i] in node:
                    node = node[word[i]]
                    # the word is end and it can be matched -> dfs [matched oooo] [remaining part of word]
                    if '#' in node and dfs(word,i+1,root.nodes,visited):
                        return True
                else:
                    break
            visited[j] = 1
            return False

            
        # If the word can be composed by other words
        def check(word):
            visited = [0 for i in range(len(word))]
            return dfs(word,0,root.nodes,visited)

        # Create the Prefix tree
        for word in words:
            if check(word) and word!='':
                res.append(word)
            root.insert(word)
        return res





        
if __name__=="__main__":
    # words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    # check empty 
    # words = ['']
    words = ["a","aa","aaa","aaab"]
    a = Solution()
    a.findAllConcatenatedWordsInADict(words)