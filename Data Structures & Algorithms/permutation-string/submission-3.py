class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_1 = {}
        for char in s1 :
            hash_1[char] = hash_1.get(char,0) + 1
        hash_2 = {}
        l=0
        r=len(s1) - 1
        while r < len(s2) :
            for i in range(l,r+1) :
                hash_2[s2[i]] = hash_2.get(s2[i],0) + 1
            if hash_2 == hash_1 :
                return True
            r += 1
            l += 1
            hash_2 = {}
        return False