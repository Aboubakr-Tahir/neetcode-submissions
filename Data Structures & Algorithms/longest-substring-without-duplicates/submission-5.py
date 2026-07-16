class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hash_set = set()
        max_length = 0
        for r in range(len(s)) :
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l += 1
            hash_set.add(s[r])
            max_length = max(max_length,len(hash_set))
        return max_length