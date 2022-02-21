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
  ----------------------------------------------------------------------------------------------------------
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        'R......R' => 'RRRRRRRR'
        'R......L' => 'RRRRLLLL' or 'RRRR.LLLL'
        'L......R' => 'L......R'
        'L......L' => 'LLLLLLLL'
        Runtime: 318 ms, faster than 87.50% of Python online submissions for Push Dominoes.
        Memory Usage: 21.6 MB, less than 25.00% of Python online submissions for Push Dominoes.
        """
        dominoes = "L" + dominoes + "R"
        res = []
        l = 0
        for r in range(1,len(dominoes)):
            if dominoes[r] == '.':
                continue
            mid = r-l-1
            print(mid)
            if l!=0: #add current except
                res.append(dominoes[l])
            if dominoes[l] == dominoes[r]:
                res.append(dominoes[l]*mid)
            elif dominoes[l] == 'L' and dominoes[r] == 'R':
                res.append('.'*mid)
            else:
                res.append('R'*(mid//2)+'.'*(mid%2)+'L'*(mid//2))
            l = r
        return "".join(res)
