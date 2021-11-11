"https://blog.csdn.net/fuxuemingzhu/article/details/80680454"

import collections
import heapq
class ASolution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        贪心
        使用内置计数器，取出现次数最多的字符(counter_most_common())
        且 counter_most_common()[0]!=arr[-1]添加至res
        当前字符串个数-1，为0时从count中删除
        
        1> count 为空，可组成res， return
        2> 某个元素一直存在，死循环 -> 
           增加stop条件，遍历count，
           当counter_most_common()[0]!=arr[-1]时，可继续执行，
           遍历完毕，仅剩重复值，结束循环 return""
        """
        counter = collections.Counter(S)
        ans = "#"
        while counter:
            print(counter)
            stop = True
            for item, times in counter.most_common():
                print(item, times)
                if ans[-1] != item:
                    ans += item
                    counter[item] -= 1
                    print(ans)
                    if not counter[item]:
                        del counter[item]
                    stop = False
                    break
            if stop: break
        return ans[1:] if len(ans) == len(S) + 1 else ""

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        python 的堆是小根堆，若要pop出现次数最多，则取负值

        构建heap, pop两次，保证res添加的元素是不一样的
        (注意len(heap)为１的情况，使用cnt来判断对pop次数)
        用temp 保存变量，添加至heap再次构建小根堆

        1> return res
        2> pop 后，heap为空，说明已无其它不同字母，则结束循环 return ""

        """
        _len = len(S)
        count = collections.Counter(S)
        que = [(-v, c) for c, v in count.items()]
        heapq.heapify(que)
        res = ""
        while _len:
            cnt = min(_len, 2)
            temp = list()
            print("_len",_len)
            print("cnt",cnt)
            print("temp",temp)
            for i in range(cnt):
                if not que:
                    return ""
                v, c = heapq.heappop(que)
                res += c
                if v + 1 != 0:
                    temp.append((v + 1, c))
                _len -= 1
            for x in temp:
                heapq.heappush(que, x)
        return res

a = Solution()
print(a.reorganizeString(S='lflxllb'))