class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r , l = 0 , 0
        res = 0
        count = {}
        while r < len(s) :
            for i in range(l,r + 1) :
                count[s[i]] = count.get(s[i],0) + 1
            max_count = 0
            for value in count.values() :
                max_count = max(max_count,value)
            if (r - l + 1) - max_count <= k :
                res = max(res,(r-l+ 1))
                r += 1
                count = {}
            else : 
                l += 1
                count = {}
        return res