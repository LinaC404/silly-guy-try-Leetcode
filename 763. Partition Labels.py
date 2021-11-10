from collections import defaultdict

class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = []
        filter = []
        index_dict = defaultdict(list)
        for i in range(len(s)):
            index_dict[s[i]].append(i)
        print(index_dict)
        for key,val in index_dict.items():
            i,j = val[0],val[-1]
            flag = 0
            print(key)
            for next_key,next_val in index_dict.items():
                if next_key not in filter:
                    m,n = next_val[0],next_val[-1]
                    if n<i or m>j:
                        pass
                    else:
                        i = min(i,m)
                        j = max (j,n)
                        filter.append(next_key)
                        print("add",next_key)
                        print(i,j)
                        temp = j-i+1
                        if temp>flag:
                            flag = temp
            res.append(flag)
        return [i for i in res if i!=0]
                


if __name__=="__main__":
    s = "caedbdedda"
    a = Solution()
    print(a.partitionLabels(s))
