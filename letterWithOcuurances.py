s = "www.google.com"
d = dict()
for char in s:
    if d.get(char) != None:
        d[char] += 1
    else:
        d[char] = 1

for key in d.keys():
    print(key,"--->",d[key])
