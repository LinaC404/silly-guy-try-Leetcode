from collections import defaultdict
class Solution(object):
    def myminCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        Runtime: 45 ms, faster than 6.82% of Python online submissions for Minimum Cost to Move Chips to The Same Position.
        Memory Usage: 13.5 MB, less than 36.36% of Python online submissions for Minimum Cost to Move Chips to The Same Position.
        """
        ans = float("inf")
        pos_dict = defaultdict(int)
        pos = set()
        for p in position:
            pos_dict[p] += 1
            pos.add(p)
        print(pos_dict)

        for i in pos:
            temp = 0
            for p,v in pos_dict.items():
                if p==i:
                    continue
                else:
                    temp += ((p-i)%2)*v
            ans = min(ans,temp)
        return ans
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        Runtime: 21 ms, faster than 82.95% of Python online submissions for Minimum Cost to Move Chips to The Same Position.
        Memory Usage: 13.4 MB, less than 70.45% of Python online submissions for Minimum Cost to Move Chips to The Same Position.
        """
        even_cost =0
        odd_cost =0
        for p in position:
            if p%2 ==0:
                even_cost+=1
            else:
                odd_cost+=1
            
        return min(even_cost,odd_cost)


        
if __name__=="__main__":
    position = [1,2,3]
    a = Solution()
    print(a.minCostToMoveChips(position))