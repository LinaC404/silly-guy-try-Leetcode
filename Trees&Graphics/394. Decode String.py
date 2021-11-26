class Solution(object):
    def mydecodeString(self, s):
        """
        :type s: str
        :rtype: str
        Runtime: 12 ms, faster than 94.38% of Python online submissions for Decode String.
        Memory Usage: 13.7 MB, less than 8.10% of Python online submissions for Decode String.
        """
        stack = []
        res = []
        i = 0
        def number_check():
            times = ""
            while stack and stack[-1].isdigit():
                times = times+stack[-1]
                stack.pop()
            return int(times[::-1])

        def stack_add(i):
            while s[i]!=']':
                stack.append(s[i])
                i = i+1
                print(stack)
            return i

        def stack_pop():
            repeat = []
            char = stack.pop()
            while char!='[':
                repeat.append(char)
                char = stack.pop()
            times = number_check()
            temp = repeat*times
            if stack:
                while temp:
                    stack.append(temp.pop())
            else:
                while temp:
                    res.append(temp.pop())
    
        while i <= len(s)-1:
            if s[i].isdigit():
                j = stack_add(i)
                stack_pop()
                i = j+1
                continue
            if stack:
                j = stack_add(i)
                stack_pop()
                i = j+1
            else:
                res.append(s[i])
                i = i+1
        
        return "".join(res)
        
    def decodeString(self, s):
        """
        https://zhenyu0519.github.io/2020/06/20/lc394/
        digit    ->   num = num*10 + int(char) [Replace number_check function]
        '['      ->   append PREVIOUS substring and Times num to stack
        alphabet ->   generate the string      [intead of adding alpha one by one]
        ']'      ->   pop out PREVIOUS substring and Times to and convert to new string
        Runtime: 45 ms
        Memory Usage: 14.3 MB
        """
        num = 0
        string = ''
        stack = []
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == '[':
                stack.append(string)
                stack.append(num)
                string = ''
                num = 0
            elif char.isalpha():
                string = string+char
            elif char == ']':
                times = stack.pop()
                pre  = stack.pop()
                string = pre + times*string
        print(string)
        return string


            
s = "3[a]2[bc]"
a = Solution()
a.decodeString(s)