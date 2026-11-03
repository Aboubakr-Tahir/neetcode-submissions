class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maximum_length = 0
        hash_set = set()
        for r in range(len(s)) : 
            if s[r] in hash_set : 
                while s[r] in hash_set : 
                    hash_set.remove(s[l])
                    l += 1
            hash_set.add(s[r])
            maximum_length = max(maximum_length,len(hash_set))
        return maximum_length
            