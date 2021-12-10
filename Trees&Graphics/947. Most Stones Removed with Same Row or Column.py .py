from collections import defaultdict
class Solution(object):
    def removeStones1(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        Runtime: 1836 ms
        Memory Usage: 14.2 MB
        * union find 
        https://blog.csdn.net/liujian20150808/article/details/50848646
        if map[x]=-1 -> 独立区域
        len(stones) - 独立石头
        """
        N = len(stones)
        self.map = [-1] * N
        for i in range(N):
            for j in range(i + 1, N):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.union(i, j)
        res = N
        print(self.map)
        for i in range(N):
            if self.map[i] == -1:
                res -= 1
        print(res)
        return res
        
    def find(self, x):
        # 返回根节点
        if self.map[x] == -1:
            return x
        else:
            return self.find(self.map[x])
        # return x if self.map[x] == -1 else self.find(self.map[x])
        
    def union(self, x, y):
        # 判断xy是否联通，如返回的根节点是一样的
        # 则已经联通,否则连结两个分量 map[x] = y
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.map[fx] = fy
    def removeStones2(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        Runtime: 3228 ms, faster than 6.89% of Python online submissions for Most Stones Removed with Same Row or Column.
        Memory Usage: 14.2 MB, less than 84.14% of Python online submissions for Most Stones Removed with Same Row or Column.
        """
        stone_dict = defaultdict(list)
        for i in range(len(stones)):
            for j in range(len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    stone_dict[i].append(j)
            stone_dict[i].remove(i)
        print(stone_dict)

        visited = set()
        res = 0
        for i in range (len(stones)):
            if i not in visited:
                stack = [i]
                visited.add(i)
                while stack:
                    node = stack.pop()
                    for j in stone_dict[node]:
                        if j not in visited:
                            stack.append(j)
                            visited.add(j)
                            res += 1
        return res
                

if __name__=="__main__":
    stones =[[0,1],[1,2],[1,3],[3,3],[2,3],[0,2]]
    a =Solution()
    a.removeStones2(stones)