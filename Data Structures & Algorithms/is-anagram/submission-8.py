class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False

        hash_map_1 = {}
        hash_map_2 = {}

        for i in range(len(s)) : 
            hash_map_1[s[i]] = hash_map_1.get(s[i],0) + 1
            hash_map_2[t[i]] = hash_map_2.get(t[i],0) + 1

        return hash_map_1 == hash_map_2