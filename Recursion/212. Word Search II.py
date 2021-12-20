from collections import defaultdict
class Trie(object):
    def __init__(self):
        self.nodes = {}
    def insert(self,word):
        curr = self.nodes
        for c in word:
            if not c in curr:
                curr[c] = {}
            curr = curr[c]
        curr['#'] = word

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        Runtime: 316 ms
        Memory Usage: 15 MB
        https://www.youtube.com/watch?v=0SFerDGfH50
        """
        m,n =len(board),len(board[0])
        res = []
        words.sort()
        root = Trie()

        for word in words:
            root.insert(word)
        print(root.nodes)

        def dfs(i,j,node):
            char = board[i][j]
            curr = node[char]
            # print(curr)
            # pop in dict pop(key[,default])
            # key: the key you want to delete
            # if not exist, return the default value

            # optimization: pop, delete the word which has been visited
            is_word = curr.pop('#', False)
            if is_word:
                print(is_word)
                res.append(is_word)
                """no return here, to avoid some situation like `oath oathi oathii` 
                   there still have words even here is an end
                """
                # return
            #  mark the char as '*', because all the char can be used only once
            board[i][j] = '*'
            directions = [(0,-1),(-1,0),(0,1),(1,0)]
            # be careful about, variable name, I alwaya make mistake here
            for p,q in directions:
                nexti,nextj = i+p,j+q
                if m>nexti>=0 and n>nextj>=0 and board[nexti][nextj] in curr:
                        dfs(nexti,nextj,curr)
            # resume the original value
            board[i][j] = char
            # optimization: the current node is None, which means the word can be deleted
            if not curr:
                node.pop(char)

        for i in range(m):
            for j in range(n):
                if board[i][j] in root.nodes:
                    dfs(i,j,root.nodes)
        return res
        
if __name__ =="__main__":
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain","oathi","oathk","oathf","oate","oathii","oathfi","oathfii"]
    a = Solution()
    a.findWords(board,words)