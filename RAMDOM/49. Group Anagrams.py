class Solution(object):
    """Runtime: 8372 ms, faster than 5.00% of Python online submissions for Group Anagrams.
       Memory Usage: 17.7 MB, less than 12.50% of Python online submissions for Group Anagrams."""
    # def groupAnagrams(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     changestrs = []
    #     res = []
    #     for i in range(len(strs)):
    #         temp = []
    #         for j in range(len(strs[i])):
    #             temp.append(ord(strs[i][j]))
    #         temp.sort()
    #         changestrs.append(temp)
        
    #     for m in range(len(changestrs)):
    #         same = [strs[i] for i in range(len(changestrs)) if changestrs[i] == changestrs[m]]
    #         res.append(same)
    #     # print(res)
    #     result = []
    #     for x in res:
    #         if x not in result:
    #             result.append(x)
    #     return result
    def groupAnagrams(self, strs):
        tmp = {}
        for i in strs:
            sort_word = ''.join(sorted(i))
            # print(sort_word)
            if sort_word in tmp:
                tmp[sort_word] += [i]
            else:
                tmp[sort_word] = [i]
        #     print(tmp)
        # print(tmp.values())
        # print(type(tmp.values()))
 
        return list(tmp.values())

        


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    a = Solution()
    print(a.groupAnagrams(strs))