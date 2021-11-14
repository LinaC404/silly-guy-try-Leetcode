from collections import defaultdict
# import collections
# class MYMapSum(object):

#     def __init__(self):
#         self.prexdict = defaultdict(int)
        
#     def insert(self, key, val):
#         """
#         Runtime: 16 ms
#         :type key: str
#         :type val: int
#         :rtype: None
#         """
#         self.prexdict[key] = val
#         print(self.prexdict)

#     def sum(self, prefix):
#         """
#         :type prefix: str
#         :rtype: int
#         """
#         ans = 0
#         for word,val in self.prexdict.items():
#             print(prefix,word,word[:len(prefix)+1])
#             if prefix == word[:len(prefix)]:
#                 ans = ans + val
#         print("Answer is ",ans)
#         return ans


"""https://www.youtube.com/watch?v=FYluJaicnlY
https://blog.csdn.net/fuxuemingzhu/article/details/79436619
前缀树的构造
使用diff进行更新
"""
class Node(object):
    def __init__(self, count = 0):
        self.children = defaultdict(Node)
        self.count = count
        
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        self.keys = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        curr = self.root
        delta = val - self.keys.get(key, 0)
        # 更新保存键值对的keys
        self.keys[key] = val
        print(delta)
        print(self.keys)
        
        curr = self.root
        # 更新节点的count
        curr.count += delta
        for char in key:
            print("char",char, curr.count)
            curr = curr.children[char]
            curr.count += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                print(0)
                return 0
            curr = curr.children[char]
            print("char",char, curr.count)
        print("Answer",curr.count)
        return curr.count
        

if __name__=="__main__":
    # Your MapSum object will be instantiated and called as such:
    obj = MapSum()
    action = ["insert","sum","insert","sum","sum","insert","sum","sum","sum","insert","sum","sum","sum","sum","sum","insert","insert","insert","sum","sum","sum","sum","sum","sum","insert","sum","sum"]
    value = [["aa",3],["a"],["aa",2],["a"],["aa"],["aaa",3],["aaa"],["bbb"],["ccc"],["aewfwaefjeoawefjwoeajfowajfoewajfoawefjeowajfowaj",111],["aa"],["a"],["b"],["c"],["aewfwaefjeoawefjwoeajfowajfoewajfoawefjeowajfowaj"],["bb",143],["cc",144],["aew",145],["bb"],["cc"],["aew"],["dddd"],["cdcd"],["aab"],["aab",33],["aab"],["ab"]]
    for i in range(len(action)):
        if action[i] == "insert":
            obj.insert(value[i][0], value[i][1])
            print("INSERT",value[i][0], value[i][1])
        elif action[i] == "sum":
            obj.sum(value[i][0])
            print("QUERY",value[i][0])