from collections import defaultdict
class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        res = 0
        col_list = list(set(colors))
        color_dict = defaultdict(list)
        for index,color in enumerate(colors):
            color_dict[color].append(index)
        # print(color_dict)
        for i in range(len(col_list)):
            i_max = color_dict[col_list[i]][-1]
            i_min = color_dict[col_list[i]][0]
            # print(max_index,min_index)
            for j in range(i+1,len(col_list)):
                j_max = color_dict[col_list[j]][-1]
                j_min = color_dict[col_list[j]][0]
                # print(res,abs(i_max-j_min),abs(j_max-i_min))
                res = max(res,abs(i_max-j_min),abs(j_max-i_min))
                # print(res,abs(i_max-j_min),abs(j_max-i_min))
        return res

        # for color,indexs in color_dict.items():
        #     max_index = indexs[-1]
        #     min_index = indexs[0]
        #     for 



        
if __name__=="__main__":
    colors =  [0,1]
    a = Solution()
    a.maxDistance(colors)