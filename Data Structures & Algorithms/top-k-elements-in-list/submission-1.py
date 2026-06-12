class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_set = {}
        for num in nums : 
            hash_set[num] = hash_set.get(num , 0) + 1
        sorted_keys = sorted(hash_set, key=hash_set.get, reverse=True)
        return sorted_keys[:k]
        return res.sort()