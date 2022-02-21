from collections import defaultdict
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        TLE 42 / 43 test cases passed.
        """
        res = list(dominoes)
        state = defaultdict(list)
        for i,v in enumerate(dominoes):
            state[v].append(i)
        pairs = []
        j = 0
        for i in range(len(state['R'])):
            while j < len(state['L']):
                if state['L'][j]>state['R'][i]:
                    if pairs and pairs[-1][1] == state['L'][j]:
                        pairs.pop()
                    pairs.append([state['R'][i],state['L'][j]])
                    break
                j += 1

        for seg_l,seg_r in pairs:
            mid = (seg_l+seg_r)//2
            if (seg_l+seg_r)%2 == 0:
                for i in range(seg_l,mid):
                    res[i] = 'R'
                for j in range(mid+1,seg_r):
                    res[j] = 'L'
            if (seg_l+seg_r)%2 == 1:
                for i in range(seg_l,mid+1):
                    res[i] = 'R'
                for j in range(mid+1,seg_r):
                    res[j] = 'L'

        
        mm = set(sum(pairs,[]))
        l_wall = [-1]+[n[1] for n in pairs]+[len(dominoes)]
        r_wall = [-1]+[n[0] for n in pairs]+[len(dominoes)]
        l = sorted(list(set(state['L']) - (set(state['L'])&mm)))
        r = sorted(list(set(state['R']) - (set(state['R'])&mm)))
        p = 0
        for i in range(len(l)):
            while p < len(l_wall)-1:
                if l_wall[p] <l[i] <l_wall[p+1]:
                    for q in range(l_wall[p]+1,l[i]+1):
                        res[q] = 'L'
                    break
                p = p+1
        p = 0
        for i in range(len(r)):
            while p < len(r_wall)-1:
                if r_wall[p] <r[i] <r_wall[p+1]:
                    for q in range(r[i]+1,r_wall[p+1]):
                        res[q] = 'R'
                    break
                p = p+1
        return "".join(res)
        
        
if __name__=="__main__":
    dominoes = ".L.R...LR..L.."
    a = Solution()
    print(a.pushDominoes(dominoes))