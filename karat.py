def destinations(teleporter, dice, startPos, endPos):
    porter_map={}
    res=[]
    # initial map for teleporting back
    for i in teleporter:
        k,v = i.split(",")        
        porter_map[int(k)]=int(v)
        
    for k, v in porter_map.items():
        print(k,v)
           
    
    currpos = startPos
    
    #start looping through the possible dice values 
    dice + startPos >= endPos
    maxDice = endPos - startPos
    maxDice = dice
    for i in range(1,maxDice+1):    
        currpos= startPos+i
        print("current Position",currpos)
        if(currpos in porter_map.keys()):
            print("current Position in the map")
            print(porter_map[currpos])
            currpos = porter_map[currpos]
        if(currpos >= endPos):
            print('inside')
            res.append(currpos)
            break
        res.append(currpos) 
        deduplicateRes= set(res)
        print(deduplicateRes)
        
    return deduplicateRes
        
#res = destinations(["3,1", "4,2", "5,10"], 6, 0, 20)
#res = destinations(teleporters2,  6,   46,   100) 
teleporters3 = ["6,18", "36,26", "41,21", "49,55", "54,52",
                "71,58", "74,77", "78,76", "80,73", "92,85"]
res = destinations(teleporters3, 10,   95,   100)
print(res)