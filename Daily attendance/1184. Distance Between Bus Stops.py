class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        Runtime: 33 ms, faster than 93.10% of Python online submissions for Distance Between Bus Stops.
        Memory Usage: 14.3 MB, less than 72.41% of Python online submissions for Distance Between Bus Stops.
        """
        s = min(start,destination)
        e = max(start,destination)
        dis = sum(distance[s:e])
        return min(dis,sum(distance)-dis)
        