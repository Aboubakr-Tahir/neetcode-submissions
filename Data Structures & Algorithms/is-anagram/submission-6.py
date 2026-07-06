class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        
        hash_map_s = {}
        hash_map_t = {}

        for char in s :
            hash_map_s[char] = hash_map_s.get(char,0) + 1
        
        for char in t :
            hash_map_t[char] = hash_map_t.get(char,0) + 1
        
        if hash_map_s==hash_map_t :
            return True
        return False