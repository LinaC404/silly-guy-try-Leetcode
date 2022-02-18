class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        Runtime: 754 ms, faster than 68.73% of Python online submissions for Find Center of Star Graph.
        Memory Usage: 52.6 MB, less than 40.05% of Python online submissions for Find Center of Star Graph.
        """
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
        