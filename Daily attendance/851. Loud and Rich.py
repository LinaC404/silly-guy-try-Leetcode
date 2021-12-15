from collections import defaultdict
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        TLE
        71 / 86 test cases passed.
        """
        # if len(richer)==0: return quiet
        res = [1000 for i in range(len(quiet))]
        ans = [-1 for i in range(len(quiet))]
        graph = defaultdict(set)
        relation_dict = defaultdict(set)
        for i in range(len(quiet)): 
            graph[i].add(i)
        for j in range(len(richer)):
            relation_dict[richer[j][1]].add(richer[j][0])

        for i in range(len(quiet)):
            stack = []
            if relation_dict[i]:
                stack.extend(list(relation_dict[i]))
                while stack:
                    cur = stack.pop()
                    graph[i].add(cur)
                    if relation_dict[cur]:
                        stack.extend(list(relation_dict[cur]))
 
        for m,val in graph.items():
            for index in val:
                if res[m] > quiet[index]:
                    res[m] = quiet[index]
                    ans[m] = index
        return ans


if __name__=="__main__":
    # richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
    # quiet = [3,2,5,4,6,1,7,0]
    richer=[[0,1]]
    quiet = [0,1]
    a = Solution()
    a.loudAndRich(richer,quiet)