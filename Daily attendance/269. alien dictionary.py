from collections import defaultdict, deque
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        Runtime: 44 ms, faster than 10.57% of Python online submissions for Alien Dictionary.
        Memory Usage: 13.5 MB, less than 59.28% of Python online submissions for Alien Dictionary.
        Graph & Topological
        invalid case: 1. 'abc','ab'; 2. circle
        """
        # initialize graph and indegree
        ans = ""
        word_dict = defaultdict(set)
        in_degree = defaultdict(int)
        letter_set = set()
        _N = len(words)
        for word in words:
            for c in word:
                letter_set.add(c)
        
        for i in range(1,len(words)):
            pre,curr = words[i-1],words[i]
            n1,n2 = len(pre),len(curr)
            p1,p2 = 0,0
            diff_mark = False

            while p1<n1 and p2<n2:
                c1,c2 = pre[p1],curr[p2]
                if c1==c2:
                    p1 += 1
                    p2 += 1 
                    continue
                else:
                    # care about the duplicated indegree
                    if c2 not in word_dict[c1]:
                        word_dict[c1].add(c2)
                        in_degree[c2] += 1
                    diff_mark = True
                    break
            # invalid case 1
            if diff_mark is False and n1 > n2:
                return ""


        # Topological sorting
        de = deque([c for c in letter_set if c not in in_degree])
        while de:
            curr = de.popleft()
            ans += curr

            for neigh in word_dict[curr]:
                in_degree[neigh] -= 1
                if  in_degree[neigh]==0:
                    de.append(neigh)
        # invalid case 2
        return ans if len(ans)==len(letter_set) else ""




        


        
if __name__=="__main__":
    a = Solution()
    print(a.alienOrder(words = ["z","x","z"]))