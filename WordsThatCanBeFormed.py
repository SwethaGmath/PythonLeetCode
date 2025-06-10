from collections import defaultdict 
def countCharacters(words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
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
            print("word map for the word",word," is")
            for c,count in word_map.items():
                print(c,count)

            n = len(word)

            for i in range(n):
                if(char_map[word[i]] < word_map[word[i]]):
                    print("word cannot be formed")
                    break
                i+=1
            if(i == n):
                print("word can be formed from the chars. So adding its lenght to res", word)
                res += len(word)

            
        
        print("totla number of word lenght that can be formed is",res)

countCharacters(["cat","bt","hat","tree"],"atach")