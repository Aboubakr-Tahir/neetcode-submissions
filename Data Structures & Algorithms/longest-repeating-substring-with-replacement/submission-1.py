class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hash_map = {}
        res = 0

        for r in range(len(s)) :
            hash_map[s[r]] = hash_map.get(s[r],0) + 1
            max_freq = max(hash_map.values())

            while (r-l +1) - max_freq > k:
                hash_map[s[l]] = hash_map.get(s[l],0) - 1
                l += 1
            
            if (r-l +1) - max_freq <= k :
                res = max(res,(r-l +1))
            
        return res