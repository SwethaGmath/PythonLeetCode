a = "Hello World! We are trying to find longest even lettewrqwrtr  123 word"
#print(a)
longest_word = '00'
words = a.split(" ")
for word in words:
    #print(word)
    if (len(word) % 2 == 0 and len(word) > len(longest_word) ):
        longest_word = word

# print("longest word is", longest_word)
# print("Normal Slicing", a[3:6])
# print("left slicing", a[3:])
# print("Right slicing", a[:8])
# print(a[3:10:3])
# print(a[::-1])
print(a[-1::-1])
print(a[::])