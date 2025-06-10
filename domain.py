from collections import defaultdict
def count_domains(domains):
    dd = defaultdict(int)
    for i in domains:
        cnt, s = i.split()
        cnt = int(cnt)
        dd[s]+=cnt
        pos = s.find('.') + 1

        while(pos>0):
            dd[s[pos:]] += cnt
            pos = s.find(",", pos) +1
    
    for i , j in dd.items():
        yield f'{j} {i}'

print(count_domains(["900 google.mail.com", "1 intel.mail.com", "50 yahoo.com", "5 wiki.org"]))



