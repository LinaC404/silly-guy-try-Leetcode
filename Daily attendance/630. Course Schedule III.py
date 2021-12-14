import heapq as hq
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        抄的 妙啊↓
        https://www.youtube.com/watch?v=PTD5SaqqE-w&ab_channel=HuifengGuan
        1. Sort the list by the deadline
        2. Add the duration, if sum_duration < deadline -> ok
                              else: pop the course with the largest duration
        3. the number of heap is the answer
        """
        courses.sort(key=lambda x:x[1])

        heap = []
        days = 0
        for i in range(len(courses)):
            hq.heappush(heap,-courses[i][0])
            days -= courses[i][0]
            # print(heap,days)

            if days < -courses[i][1]:
                # the previous number of course must be ok, so we pop the course with the largest duration 
                temp = hq.heappop(heap)
                days -= temp
        return len(heap)
if __name__=="__main__":
    courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
    a = Solution()
    a.scheduleCourse(courses)