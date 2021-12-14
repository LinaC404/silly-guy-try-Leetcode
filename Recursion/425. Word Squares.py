class Node:
    def __init__(self):
        self.children = {}
        # store all the words with the same prefix to save time 
        # otherwisre, dfs is necessary
        self.words = []

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        借鉴如下，一层套一层 人失了智
        Tire
        了解前缀树的构造和应用
        https://www.youtube.com/watch?v=unLYmWQ9MVI&ab_channel=HappyCoding
        """
        def add(word):
            cur = root
            for char in word:
                if not char in cur.children:
                    cur.children[char] = Node()
                    # print(cur.children)
                    # print(cur.words)
                cur = cur.children[char]
                cur.words.append(word)
        # Build Trie 
        root = Node()
        for word in words:
            add(word)
        
        def get_candidates(prefix):
            cur = root
            for char in prefix:
                if not char in cur.children:
                    return []
                cur = cur.children[char]
            return cur.words

        # backtracking
        def backtracking(flag,cur_list):
            if flag == _N:
                # be careful of deep copy and shallow copy
                res.append(cur_list[:])
                return

            """
            e.g flag=2
                    +++
            [ b  a  +l+ l,
              a  r  +e+ a
                    +++       
            ]
            prefix = 'le'
            """
            prefix = "".join(word[flag] for word in cur_list)
            
            candidates = get_candidates(prefix)
            print(flag,candidates)
            for candidate in candidates:
                cur_list.append(candidate)
                backtracking(flag+1,cur_list)
                cur_list.pop()

        res = []
        _N = len(words[0])
        for word in words:
            backtracking(1,[word])

        return res

if __name__=="__main__":
    words = words = ["area","lead","wall","lady","ball"]
    a = Solution()
    a.wordSquares(words)
