from collections import defaultdict

dd= defaultdict(list)

dd["a"] = 'a'
dd["b"]= 'b'

print(dd)

if dd.get('a') is not None:   # check if a key exists
    print(dd['a'])

print(dd.keys()) # print all keys

for k,j  in dd.items():
    print(k,"->",j)
