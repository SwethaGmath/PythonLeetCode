s = "cat"
d ="tac"
def is_anagram(s1,s2):
    source = sorted(s1)
    dest = sorted(s2)
    if(source == dest):
        print("is anagram")
    else:
        print("not anagram")

is_anagram(s, d)

###### list of anagrams from a list of words
s =["eat","tea","tan","ate","nat","bat"]
fullres = list()
def listOfAnagrams(l):
    n = len(l)
    for i in range(n):
        res = list()
        for j in range(i+1, n):
            if(sorted(l[i]) == sorted(l[j])):
                res.append(l[j])
        fullres.append(res)
    return fullres

res = listOfAnagrams(s)
print(res)


