from collections import defaultdict
class Trie(object):
    def __init__(self):
        self.nodes = {}
        self.is_word = False
    def insert(self,word):
        curr = self.nodes
        for c in word:
            if not c in curr:
                curr[c] = {}
            curr = curr[c]
        curr[self.is_word] = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str
        
        """
        words.sort()
        root = Trie()
        for word in words:
            root.insert(word)
        print(root.nodes)

        start_dict = defaultdict(list)
        m,n = len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                start_dict[board[i][j]].append([i,j])
        print(start_dict)

        word_list = []

        def search(index,i,j,word):
            # dfs 进行遍历，下一个字母的索引是都在start_index 中，继续查找 否则返回false

            directions = [(-1,0),(0,1),(1,0),(0,-1)]
            for c in word:
                pass
        
        def startwith(word):
            # 遍历前缀树
            # 调用 search function 若遍历至True 则存在，添加至结果
            pass
        
if __name__ =="__main__":
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain","oaan","oate"]
    a = Solution()
    a.findWords(board,words)