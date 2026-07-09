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
            if len(res) == k :
                break
            for num in freq[i] :
                if len(res) == k :
                    break
                res.append(num)
        return res 