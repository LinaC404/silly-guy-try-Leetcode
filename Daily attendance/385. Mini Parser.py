# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        Runtime: 75 ms, faster than 83.25% of Python3 online submissions for Mini Parser.
        Memory Usage: 17.4 MB, less than 95.43% of Python3 online submissions for Mini Parser.
        """
        stack = []
        i = 0
        temp = ""
        while i<len(s):
            if s[i] == "[":
                stack.append(NestedInteger())
            elif s[i].isdigit() or s[i]=="-":
                temp += s[i]
            elif (s[i]=="," or s[i]=="]")and temp:
                stack[-1].add(NestedInteger(int(temp)))
                temp = ""
            if s[i]=="]" and len(stack)>1:
                curr = stack.pop()
                stack[-1].add(curr)
            i += 1
    
        if temp:
            stack.append(NestedInteger(int(temp)))
        return stack[-1]


                

    

                 
