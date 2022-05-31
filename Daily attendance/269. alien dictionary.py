from collections import defaultdict
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.ans = ""
        word_dict = defaultdict(list)
        indgree = defaultdict(int)
        visited = set()
        for i in range(1,len(words)):
            if words[i][0] == words[i-1][0]:
                j = 1
                while j < len(words[i]) and j < len(words[i-1]):
                    if words[i][j] == words[i-1][j]:
                        pass
                    else:
                        word_dict[words[i-1][j]].append(words[i][j])
                        indgree[words[i-1][0]]
                        indgree[words[i][j]] += 1
                    j += 1
            else:
                word_dict[words[i-1][0]].append(words[i][0])
                indgree[words[i-1][0]]
                indgree[words[i][0]] += 1
            
        start = []
        for char,ind in indgree.items():
            if ind == 0:
                start.append(char)

        if len(start)==0: return ""

        # print(word_dict)
        def dfs(curr,visited):
            self.ans += curr
            # print(self.ans)
            visited.add(curr)
            # print("Next",word_dict[curr])
            for n_elem in word_dict[curr]:
                indgree[n_elem] -= 1
                if indgree[n_elem]==0 and n_elem not in visited:
                    del indgree[n_elem]
                    # print(indgree)
                    dfs(n_elem,visited)


        for s in start:
            del indgree[s]
            dfs(s,visited)
        return self.ans


        


        
if __name__=="__main__":
    a = Solution()
    print(a.alienOrder(words = ["z","z"]))