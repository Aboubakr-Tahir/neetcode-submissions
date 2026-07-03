class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longuest = 0
        for n in nums :
            if (n-1) not in hash_set :
                length = 0
                while n + length in hash_set :
                    length += 1
                longuest = max(longuest,length)
        return longuest