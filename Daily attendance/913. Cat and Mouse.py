class Solution(object):
    def catMouseGame1(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        https://www.youtube.com/watch?v=oGKnucI_ejw&ab_channel=HappyCoding
        https://www.acwing.com/solution/leetcode/content/556/
        (动态规划) O(n2m)O(n2m)
        设状态 f(x,y,t)   f(x,y,t) 表示 t 时刻，老鼠位于 x 且猫位于 y 时的结果（0/1/2）。

        如果当前为老鼠行动，那么他可以走到 f(t+1,i,y),i∈graph[x]，如果他走到的这些点结果都是 2，则老鼠必输无疑；
        若其中有一个是 1，则老鼠必获胜；否则结果就是平局。
        对于猫来说，以上分析相反。

        我们已经知道的状态有，f(0,y,t)=1，f(x,x,t)=2 分别代表老鼠获胜和猫获胜。

        若游戏进行了 2n个单位时间还没有结束，则可以宣布平局（待证明，以下为直觉想法）。
        因为每一次移动老鼠都有可能到达一个新的位置，所以它最多只需要 2n 步就可能找到出口（因为猫对应也走了 n 步）。
        若超过了 2n步，则老鼠必定走了回头路，此时不管猫在哪，走回头路都是向猫 “妥协” 的选择；
        同理对猫来说，走回头路也是向老鼠 “妥协” 的结果；故最大的 t 只需要 2n 即可。
        我们从 solve(1,2,0) 开始记忆化搜索即可。

        """
        # top down (m,c,times)
        # if the move time > 2*nodes ->repeated path -> draw           0
        # same node                                  -> cat wins       2
        # mouse reach node 0                         -> mouse wins     1
        _N = len(graph)                
        dp = [[[-1 for i in range(_N*2)] for j in range(_N)] for q in range(_N)]
        def game(m,c,times):
            print(m,c,times)
            if times == 2*_N:
                return 0
            if m==c:
                dp[m][c][times]=2
                return 2
            if m==0:
                dp[m][c][times]=1
                return 1
            if dp[m][c][times]!=-1:
                return dp[m][c][times]

            if times%2 == 0:
                catWin = True
                for nei in graph[m]:
                    ans = game(nei,c,times+1)
                    if ans == 1:
                        dp[m][c][times] = 1
                        return 1
                    elif ans !=2 :
                        catWin = False
                if catWin:
                    dp[m][c][times] = 2
                    return 2           
                else:
                    dp[m][c][times] = 0
                    return 0
            else:
                mouseWin = True
                for nei in graph[c]:
                    if nei != 0:
                        ans = game(m,nei,times+1)
                        if ans == 2:
                            dp[m][c][times] = 2
                            return 2
                        elif ans!=1 :
                            mouseWin = False
                if mouseWin:
                    dp[m][c][times] = 1
                    return 1
                else:
                    dp[m][c][times] = 0
                    return 0

        return game(1,2,0)

        

    def catMouseGame2(self, graph):
        # [[6],[4],[9],[5],[1,5],[3,4,6],[0,5,10],[8,9,10],[7],[2,7],[6,7]]
        # Error
        def search(x, y, t):
            print(x,y,t)
            if t == len(graph) * 2: return 0
            if x == y: return 2
            if x == 0:return 1
            if (t%2==0):# mouse's turn. Mouse will win if the mouse can find any winable node for the next step. If all the next step is winable for cats, then mouse lose.
                if any(search(x_nxt, y, t+1)==1 for x_nxt in graph[x]):return 1
                if all(search(x_nxt, y, t+1)==2 for x_nxt in graph[x]):return 2
                return 0
            else:# cat's turn
                if any(search(x, y_nxt, t+1)==2 for y_nxt in graph[y] if y_nxt!=0):return 2
                if all(search(x, y_nxt, t+1)==1 for y_nxt in graph[y] if y_nxt!=0):return 1
                return 0
        return search(1, 2, 0)



if __name__=="__main__":
    graph = [[6],[4,11],[9,12],[5],[1,5,11],[3,4,6],[0,5,10],[8,9,10],[7],[2,7,12],[6,7],[1,4],[2,9]]
    a = Solution()
    print(a.catMouseGame2(graph))

        