from collections import Counter
from datetime import datetime
def alertNames(keyName, keyTime):
    """
    :type keyName: List[str]
    :type keyTime: List[str]
    :rtype: List[str]
    """
    nameCnt = Counter(keyName)
    i = 0
    n = len(keyName)
    res = []
    
    def is_within_1hr(t1, t2):
        time_format = "%H:%M"
        time1_obj = datetime.strptime(t1, time_format)
        time2_obj = datetime.strptime(t2, time_format)
        time_diff = abs((time2_obj - time1_obj).total_seconds() / 60)
        print(time_diff)
        if time_diff <= 60:
            return True
        else:
            return False
        # h1, m1 = t1.split(":")
        # h2, m2 = t2.split(":")
        # if int(h1) + 1 < int(h2): return False
        # if h1 == h2: return True
        # return m1 >= m2
    
    while ( i < n ):
        print("i is", i)
        name = keyName[i]
        print("current name is,", name)
        print("current name's count is,", nameCnt[name])
        nameTracker = 1
        j = i
        runtime = 1
        while ( runtime < nameCnt[name]):
        #for j in range(i,nameCnt[name] -1):
            start = keyTime[j]
            print("start time is", start)
            end = keyTime[j+1]
            print("end time is",end)
            if is_within_1hr(start, end):
                nameTracker+=1
                if(nameTracker>=3):
                    print(name," has used card within one hour")
                    res.append(name)
            j+=1
            runtime+=1
        i += nameCnt[name]
    return res

res = alertNames( ["alice","alice","alice","bob","bob","bob","bob"], ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]) 
print(res)