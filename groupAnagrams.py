def anagrams(self, arr):
        '''
        
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        n = len(arr)
        res= []
        seen = {}
        for i in range( 0, n):
            curr = arr[i]
            currList=[]
            if( curr in seen):
                continue
            currList.append(curr)
            for j in range(i+1, n):
                if sorted(curr) == sorted(arr[j]):
                    currList.append(arr[j])
                    seen[arr[j]] = True
            res.append(currList)
        return res