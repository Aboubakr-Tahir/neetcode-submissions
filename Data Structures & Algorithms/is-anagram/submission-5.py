class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : 
            return False
        #create hashmap of the s string    
        s_hash_map = {} 
        for char in s : # O(n) speed
            #O(n) spatial
            if char not in s_hash_map :  
                s_hash_map[char] = 1
            else : 
                s_hash_map[char] += 1
        #create hashmap of the t string 
        t_hash_map = {} 
        for char in t : 
            if char not in t_hash_map : 
                t_hash_map[char] = 1
            else : 
                t_hash_map[char] += 1
        
        for key , value in s_hash_map.items() : 
            if key not in t_hash_map : 
                return False
            if value != t_hash_map[key] :
                return False
        return True

        