class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        https://www.youtube.com/watch?v=oGKnucI_ejw&ab_channel=HappyCoding
        """
        # top down TLE 
        # if the move time > 2*nodes ->repeated path -> draw
        # same node                                  -> cat wins
        # mouse reach node 0                         -> mouse wins

        def dp (m,c,moves):
            print(m,c,moves)
            if moves > 2*len(graph):
                return 0
            if m == c: 
                return 2
            if m == 0: 
                return 1
            # mouse turn 
            if moves%2 == 0:
                canDraw = False
                for nei in graph[m]:
                    ans =  dp(nei,c,moves+1)
                    if ans == 1:
                        return 1
                    if ans == 0:
                        canDraw = True
                if canDraw: 
                    return 0
                else: 
                    return 2
            #cat turns
            else:
                canDraw = False
                for nei in graph[c]:
                    if nei == 0:
                        continue
                    ans = dp(m,nei,moves+1)
                    if ans == 2:
                        return 2
                    if ans == 0:
                        canDraw = True
                if canDraw:
                    return 0
                else:
                    return 1
        
        return dp(1,2,0)


if __name__=="__main__":
    graph = [[6],[4,11],[9,12],[5],[1,5,11],[3,4,6],[0,5,10],[8,9,10],[7],[2,7,12],[6,7],[1,4],[2,9]]
    a = Solution()
    print(a.catMouseGame(graph))

        