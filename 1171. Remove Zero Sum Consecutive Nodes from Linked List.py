# Definition for singly-linked list.
from collections import defaultdict
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MySolution(object):
    def removeZeroSumSublists(self, head):
        """
        Runtime: 124 ms, faster than 14.50% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
        Memory Usage: 15 MB, less than 6.80% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
        :type head: ListNode
        :rtype: ListNode
        """
        mylist = []
        p = head
        while p:
            mylist.append(p.val)
            p=p.next

        if len(mylist)==1:
            if mylist[0]==0:
                return None
            else:
                return head

        sumlist = [mylist[0]]
        for i in range(1,len(mylist)):
            sumlist.append(mylist[i]+sumlist[i-1])
        print(sumlist)

        sum_dict = defaultdict(list)
        for index,val in enumerate(sumlist):
            sum_dict[val].append(index)
        print(sum_dict)

        stop = True
        if sum_dict[0]:
            end = sum_dict[0][-1]
            if end == len(mylist):
                return None
            else:
                sumlist = sumlist[end+1:]
                mylist = mylist[end+1:]
        else:
            del sum_dict[0]
        while stop:
            temp = 0
            for i in range(1,len(sumlist)):
                if sumlist[i] in sumlist[:i]:
                    index  = sumlist[:i].index(sumlist[i])
                    print(index)
                    sumlist = sumlist[:index+1]+sumlist[i+1:]
                    mylist = mylist[:index+1]+mylist[i+1:]
                    print(sumlist)
                    temp = 1
                    break
            if temp == 0:
                stop = False

        ans = [i for i in mylist if i!=0]
        # print("Answer",ans)
        if len(ans)==0:
            return None
        else:
            res =  ListNode(ans[0])
            p = res
            for n in range(1,len(ans)):
                node = ListNode(ans[n])
                p.next = node
                p = p.next
        return res
"""https://zxi.mytechroad.com/blog/list/leetcode-1171-remove-zero-sum-consecutive-nodes-from-linked-list/
Runtime: 36 ms, faster than 95.27% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
Memory Usage: 14.6 MB, less than 74.26% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
"""
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        def helper(head: ListNode):      
            dummy = ListNode(0)
            dummy.next = head
            prev, curr = dummy, dummy.next    
            s = 0
            m = {s: prev}
            done = True
            while curr:
                s += curr.val
                if s in m:
                    m[s].next = curr.next
                    # 表示当前已经更新过链表，以此为依据判断
                    # 若已经更新过，则整个链表还需要再次判断，
                    # 否则表示不存在相同值，不包含为0的相邻链表，可以结束循环
                    done = False
                else:
                    m[s] = curr
                prev, curr = curr, curr.next
            return dummy.next, done

        while True:
            head, done = helper(head)
            if done: return head

            
        
if __name__=="__main__":
    # data = [-3,-1,1,-1,-4,1,-3,-1,3,3]
    data = [1,2,-3,3,1]
    head =  ListNode(data[0])
    p = head
    for n in range(1,len(data)):
        node = ListNode(data[n])
        p.next = node
        p = p.next
    a = Solution()
    print(a.removeZeroSumSublists(head))