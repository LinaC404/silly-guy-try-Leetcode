# import Levenshtein as L
from collections import defaultdict
class Solution(object):
    def myladderLength(self, beginWord, endWord, wordList):
        """
        Status: Time Limit Exceeded
        23/49
        :(
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not endWord in wordList: return 0
        res = []
        def compare(word1, word2):
            diff = 0
            for i in range(len(word1)):
                if word1[i]!=word2[i]:
                    diff = diff+1
            return diff

        def findnext(word,vistied,times):
            print(word,vistied,times)
            if word==endWord: 
                res.append(times)
                return times
            if list(set(vistied))==[1]: 
                res.append(0)
                return 0
            templist = []
            for j in range(len(wordList)):
                if vistied[j]==0:
                    if compare(word, wordList[j])==1:
                        templist.append([j,wordList[j]])

            vistied_temp = vistied[:]
            for m in templist:
                vistied_temp[m[0]]=1
                findnext(m[1],vistied_temp,times+1)
                vistied_temp = vistied[:]
    
        vistied = [0 for i in wordList]
        times = 1
        findnext(beginWord,vistied,times)
        if list(set(res))==[0]:
            return 0
        else:
            return min([i for i in res if i!=0]) if len(res)!=0 else 0

    def ladderLength(self, beginWord, endWord, wordList):
        """
        Runtime: 216 ms
        https://zxi.mytechroad.com/blog/searching/127-word-ladder/
        Bidirectional BFS
        if word in s1 existed in s2 return ans
        hit->hot->dot<-dog<-cog
       s1 ----------
                 --------------s2
        """
        word_dict = set(wordList)
        if not endWord in word_dict: return 0 
        # print(wordList)
        len_b = len(beginWord)
        s1 = {beginWord}
        s2 = {endWord}
        word_dict.remove(endWord)
        step = 0

        while s1 and s2:
            step = step+1
            # Make balence betwwen s1 and s2 to reducw the run time.
            if len(s1)>len(s2): s1,s2=s2,s1
            s = set()

            for word in s1:
                # e.g hit -> [ait,...,zit,hat,...<strong>hot</strong>,hzt,hia,...hiz]
                expand_words = [word[:i]+chr(c)+word[i+1:] for c in range(97, 123) for i in range(len(word))]
                for expand_W in expand_words:
                    if expand_W in s2:
                        # find the answer
                        return step+1 
                    if not expand_W in word_dict:
                        # pass
                        continue
                    # to reduce the repicated tranformation from the same word
                    word_dict.remove(expand_W)
                    # add the next_possible_words in the word_dict into s
                    s.add(expand_W)

                s1 = s
        return 0
        






if __name__=="__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    # beginWord = "qa"
    # endWord = "sq"
    # wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
    a = Solution()
    print(a.ladderLength(beginWord,endWord,wordList))
