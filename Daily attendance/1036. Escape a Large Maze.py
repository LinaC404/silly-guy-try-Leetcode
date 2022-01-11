import numpy as np
class Solution(object):
    def isEscapePossible1(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        This is a hard problem, I should show my respect...
        
        https://www.youtube.com/watch?v=O3Y67a8bc00&ab_channel=StanfordUniversitySchoolofEngineering
        Runtime: 1460 ms, faster than 7.41% of Python online submissions for Escape a Large Maze.
        Memory Usage: 47.6 MB, less than 5.55% of Python online submissions for Escape a Large Maze.
        """
        # my naive thought, if the source was enclosed by the blocked list ✕
        """
        10^6 Normal dfs -> TLE
        * Manhattan distance (source, current) > 200 --->  not be blocked
        * Both target and source are not blocked ---> return True 
        """
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        blocked = set(map(tuple, blocked))
        def dfs(start,end,curr,visited):
            if curr[0]==end[0] and curr[1]==end[1]: return True
            if np.sum(np.abs(np.array(start)-np.array(curr))) > 200: return True
            visited.add(curr)
            for i,j in directions:
                nexti,nextj = curr[0]+i,curr[1]+j
                if 0<=nexti<1000000 and 0<=nextj<1000000 and (nexti,nextj) not in visited and (nexti,nextj) not in blocked:
                    if dfs(start,end,(nexti,nextj),visited):
                        return True
            return False

        return dfs(source,target,tuple(source),set()) and dfs(target,source,tuple(target),set())



    def isEscapePossible2(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        Runtime: 144 ms, faster than 88.89% of Python online submissions for Escape a Large Maze.
        Memory Usage: 16.1 MB, less than 68.52% of Python online submissions for Escape a Large Maze.
        """
        blocked = set(map(tuple, blocked))
        def bfs(s, t): 
            """Return True if (x, y) is not looped from (tx, ty)."""
            seen = {(s[0], s[1])}
            stack = [(s[0], s[1])]
            while stack: 
                x, y = stack.pop()
                if abs(x - s[0]) + abs(y - s[1]) > 200 or (x, y) == (t[0], t[1]): return True 
                for xx, yy in (x-1, y), (x, y-1), (x, y+1), (x+1, y): 
                    if 0 <= xx < 1e6 and 0 <= yy < 1e6 and (xx, yy) not in blocked and (xx, yy) not in seen: 
                        seen.add((xx, yy))
                        stack.append((xx, yy))
            return False 
        
        return bfs(source, target) and bfs(target, source)



if __name__=="__main__":
    blocked = [[100059,100063],[100060,100064],[100061,100065],[100062,100066],[100063,100067],[100064,100068],[100065,100069],[100066,100070],[100067,100071],[100068,100072],[100069,100073],[100070,100074],[100071,100075],[100072,100076],[100073,100077],[100074,100078],[100075,100079],[100076,100080],[100077,100081],[100078,100082],[100079,100083],[100080,100082],[100081,100081],[100082,100080],[100083,100079],[100084,100078],[100085,100077],[100086,100076],[100087,100075],[100088,100074],[100089,100073],[100090,100072],[100091,100071],[100092,100070],[100093,100069],[100094,100068],[100095,100067],[100096,100066],[100097,100065],[100098,100064],[100099,100063],[100098,100062],[100097,100061],[100096,100060],[100095,100059],[100094,100058],[100093,100057],[100092,100056],[100091,100055],[100090,100054],[100089,100053],[100088,100052],[100087,100051],[100086,100050],[100085,100049],[100084,100048],[100083,100047],[100082,100046],[100081,100045],[100080,100044],[100079,100043],[100078,100044],[100077,100045],[100076,100046],[100075,100047],[100074,100048],[100073,100049],[100072,100050],[100071,100051],[100070,100052],[100069,100053],[100068,100054],[100067,100055],[100066,100056],[100065,100057],[100064,100058],[100063,100059],[100062,100060],[100061,100061],[100060,100062]]
    source = [100079,100063]
    target = [999948,999967]
    a = Solution()
    print(a.isEscapePossible(blocked,source,target))