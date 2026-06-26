class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) :
            return False
        windwow_len = len(s1)
        count1 = {}
        for char in s1 :
            count1[char] = count1.get(char,0) + 1
        
        count2 = {}
        l=0
        r = windwow_len - 1
        for i in range(r + 1) :
            count2[s2[i]] = count2.get(s2[i],0) + 1
        
        while r < len(s2) :
            if count1 == count2 :
                return True
            
            if count2[s2[l]] - 1 == 0 :
                count2.pop(s2[l])
            else :
                count2[s2[l]] -= 1

            r+=1
            if r < len(s2) :
                count2[s2[r]] = count2.get(s2[r],0) + 1
            l+=1
        return False