from collections import defaultdict
class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        https://www.youtube.com/watch?v=BIBN-vYO4Gk
        Runtime: 2177 ms, faster than 41.97% of Python3 online submissions for Count Nodes With the Highest Score.
        Memory Usage: 117.7 MB, less than 41.67% of Python3 online submissions for Count Nodes With the Highest Score.
        """
        _N = len(parents)
        children = defaultdict(list)
        scoredict = defaultdict(int)

        for i,j in enumerate(parents):
            children[j].append(i)
        del children[-1]

        def dfs(node):
            sub = []
            total = 0
            for child in children[node]:
                sub.append(dfs(child))
                total += sub[-1]
            score = 1
            if _N-1-total!=0:
                score = score*(_N-1-total)
            for sub_count in sub:
                score*=sub_count

            scoredict[score]+=1

            return total+1

        dfs(0)
        return max(scoredict.items(), key=lambda x: x[0])[1]
