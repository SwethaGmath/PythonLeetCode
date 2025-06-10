from collections import Counter


def countCharacters( words, chars):
    """
    :type words: List[str]
    :type chars: str
    :rtype: int
    """
    res = 0
    char_map = Counter(chars)
    for w in words:
        flag = True
        word_map = Counter(w)
        for c in w:
            if(char_map[c] < word_map[c]):
                flag = False
                break
        if(flag):
            print(w," can be formed, soadding its lenght")
            res += len(w)
    print("totla word lenghtthat can be formed is", res)

    
countCharacters(["cat","bt","hat","tree"],"atach")



res = 0
        char_map = defaultdict(int)
        for char in chars:
            char_map[char] += 1
        print("char map is:")
        for c,count in char_map.items():
             print(c,count)

        for word in words:
            word_map=defaultdict(int)
            for c in word:
                word_map[c]+=1

            n = len(word)

            for i in range(n):
                if(char_map[word[i]] < word_map[word[i]]):
                    break
                i+=1
            if(i == n):
                res += len(word)
            
        return res