class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_set1 = {}
        hash_set2 = {}

        for i in s : 
            hash_set1[i] = hash_set1.get(i,0) + 1

        for i in t : 
            hash_set2[i] = hash_set2.get(i,0) + 1

        if hash_set1 == hash_set2 :
            return True
        
        return False