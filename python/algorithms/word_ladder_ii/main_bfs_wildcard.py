#!/usr/bin/env python3

from collections import deque
from collections import defaultdict


# A BEAST !!!!
# The Upgrade of alphabet bfs
#complexity O(n*m) with m size of the word; n number of words in wordlist

#instead of doing a permutation of all letter, i use *
# for example look at the word hok as begin word and wordlist = hak hik pok pik hko 
# instead of changing all letter of hok we can just do hok: *ok, h*k, ho*
# and we see that the transformation of hak (h*k), hik (h*k), pok(*ok) are corresponding to hok
# they are its neighor doing just 3 permutations.

# We transform all words to find their neighbor and then do a bfs 

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        if not endWord in wordList:
            return []
        to_see = deque([(beginWord, "",0)])
        count = 0
        dist = 1
        res = []
        size_word = len(beginWord)
        range_size_word = range(size_word)
        # to increase the speed, i used a dictionary. Stop using array or list to visited
        #use instead, dictionary or set
        visited = defaultdict(set)
        #h*a will have as values hoa, hia, hla for exemple
        patternDict = defaultdict(list)
        #all possibilities of words
        wordPossibilites = defaultdict(list)
#        wordList.appendd(beginWord)
        if beginWord not in wordList:
            wordList.append(beginWord)
        for word in wordList:
            for j in range_size_word:
                pattern = word[:j] + "*" +word[j + 1:]
                patternDict[pattern].append(word)
                wordPossibilites[word].append(pattern)
        # BFS hehe
        while (to_see and res == []):
            size = len(to_see)
            print(dist)
            dist+=1
#            print(to_see)
            while (size):
                current, path, nbr = to_see.pop()
                path += (current + " ")
#                visited[nbr] = visited[nbr].copy()
#                visited[nbr - 1].clear()
#                print(visited[nbr])
                for pattern in wordPossibilites[current]:
                    if not pattern in visited[nbr]:
                        for word in patternDict[pattern]:
                            if word == endWord:
                                res.append((path + endWord).split(" "))
#                                visited[nbr].add(word)
                                break
                            if not word in visited[nbr]:
    #                                set_path.add(pattern)
    #                                set_path.add(word)
                                visited[nbr].add(word)
                                count += 1
                                to_see.appendleft((word, path[:], count))
                                visited[count] = visited[nbr].copy()
                                visited[nbr].add(pattern)
                                visited[count].add(word)
                                visited[count].add(pattern)
                        visited[nbr].add(pattern)
#                    print(count)
 #                   if count >= 1000000:
 #                       count = 0
                size -=1
        return res

sol = Solution()

beginWord = 'hot'
endWord = 'dog'
wordList = ["hot","dog"]
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
beginWord = "qa"
endWord = "sq"
wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
beginWord = "cet"
endWord = "ism"
wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim"]
beginWord = "hae"
endWord = "hij"
wordList = ["hie","hap","hip","hij","haj", "tic", "toc", "hij", "hae"]

print(sol.findLadders(beginWord, endWord, wordList))