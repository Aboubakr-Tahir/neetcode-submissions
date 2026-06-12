class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} 
        for i , num in enumerate(nums) :
            diff = target - num
            if diff in hash_map : 
                return [ min(i, hash_map[diff]), 
                         max(i, hash_map[diff]) ]
            if num not in hash_map : 
                hash_map[num] = i

