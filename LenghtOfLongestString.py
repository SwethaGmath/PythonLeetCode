def longestStringLenght(s):
    n = len(s)
    mp = {}
    i = 0
    ans = 0
    for j in range(n):
        if s[j] in mp:
            i = max(i,mp[s[j]]+1)
        ans = max(ans, j -i+1)
        mp[s[j]] = j
        print(mp.items())

    return ans

print(longestStringLenght("pwwkew"))

