from collections import Counter
def charCounts(words, chars):
    #count1 = Counter(words)
    count2 = Counter(chars)

    for word in words:
        count1 = Counter(word)
        for char in word:
            if(count1[char] > count2[char]):
                print(char, "does not match, so breaking ")
                break
            else:
                print(word, "can be formed from the letters of", chars)

        # if ((count1[char] <= count2[char] for char in word)):
        #     print(word, "can be formed from the letters of", chars)
        # else:
           

charCounts(["hello","world","leetcode"],"welldonehoneyr")