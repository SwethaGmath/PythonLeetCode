from collections import defaultdict
def subdomainVisits( cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = defaultdict(int)
        for s in cpdomains:
            cnt, s = s.split()
            cnt = int(cnt)
            d[s] += cnt
            pos = s.find('.') + 1
            while pos > 0:
                d[s[pos:]] += cnt
                pos = s.find('.', pos) + 1
        for x, i in d.items():
            print(i,x)

subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
