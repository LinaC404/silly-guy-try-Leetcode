from collections import deque
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        Runtime: 71 ms, faster than 5.30% of Python3 online submissions for Minimum Genetic Mutation.
        Memory Usage: 13.9 MB, less than 41.81% of Python3 online submissions for Minimum Genetic Mutation.
        """
        queue = deque([(start,0)])
        visited = set()
        visited.add(start)
        while queue:
            curr,step = queue.popleft()
            if curr==end:
                return step
            else:
                for i in range(len(curr)):
                    for j in "ACGT":
                        newone = curr[:i]+j+curr[i+1:]
                        if newone in bank and newone not in visited:
                            visited.add(newone)
                            queue.append((newone,step+1))
        return -1




    def minMutation2(self, start, end, bank):
        """
        Runtime: 22 ms, faster than 99.13% of Python3 online submissions for Minimum Genetic Mutation.
        Memory Usage: 13.8 MB, less than 89.39% of Python3 online submissions for Minimum Genetic Mutation.
        """
        if end not in bank:
            return -1
        
        bank = set(bank)
        chars = {"A", "C", "G", "T"}
        
        queue = deque([(start, 0)])
        seen_set = {start}
        
        while queue:
            seq, step = queue.popleft()
            if seq == end:
                return step
            
            for i in range(len(seq)):
                for c in chars:
                    next_str = seq[:i] + c + seq[i+1:]
                    if next_str not in bank or next_str in seen_set:
                        continue
                    
                    if next_str == end:
                        return step + 1
                    queue.append((next_str, step+1))
                    seen_set.add(next_str)
        return -1
                  


if __name__=="__main__":
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    a = Solution()
    print(a.minMutation(start, end, bank))