class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for ele in nums :
            if ele not in hash_set :
                hash_set.add(ele)
            else : 
                return True
        
        return False