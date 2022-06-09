from collections import defaultdict
import random
class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rect = defaultdict(list)
        self._N = [i for i in range(len(rects))]
        self.weight = []
        for i,li in enumerate(rects):
            self.rect[i] = li
            self.weight.append((li[2]-li[0]+1)*(li[3]-li[1]+1))

    def pick(self):
        """
        :rtype: List[int]
        """

        pick_i = random.choices(self._N,weights=self.weight)[0]
        px =  random.randrange(self.rect[pick_i][0],self.rect[pick_i][2]+1)
        py =  random.randrange(self.rect[pick_i][1],self.rect[pick_i][3]+1)
        return [px,py] 
# -----------------------------------------------------------------------------
class Solution2:
    def __init__(self, rects):
        w = [(x2-x1+1)*(y2-y1+1) for x1,y1,x2,y2 in rects]
        self.weights = [i/sum(w) for i in accumulate(w)]
        self.rects = rects

    def pick(self):
        n_rect = bisect.bisect(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[n_rect] 
        return [random.randint(x1, x2),random.randint(y1, y2)]

        


# Your Solution object will be instantiated and called as such:
if __name__=="__main__":
    rects = [[82918473,-57180867,82918476,-57180863],[83793579,18088559,83793580,18088560],[66574245,26243152,66574246,26243153],[72983930,11921716,72983934,11921720]]
    obj = Solution(rects)
    print(obj.pick())
    print(obj.pick())