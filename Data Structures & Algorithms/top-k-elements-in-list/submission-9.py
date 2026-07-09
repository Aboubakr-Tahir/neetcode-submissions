class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums :
            hash_map[num] = hash_map.get(num,0) + 1
        freq = [[] for i in range(len(nums) + 1)]
        for key,value in hash_map.items() :
            freq[value].append(key)
        res=[]
        for i in range(len(freq)-1,0,-1) :
            for num in freq[i] :
                res.append(num)
                if len(res) == k :
                    return res