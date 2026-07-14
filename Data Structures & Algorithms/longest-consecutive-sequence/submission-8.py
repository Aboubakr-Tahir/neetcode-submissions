class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        nums.sort()
        longuest_sequence = -float('inf')
        length = 1
        for i in range(len(nums)-1) :
            if nums[i] == nums[i + 1] :
                continue
            if nums[i] + 1 == nums[i+1] :
                length += 1
            if nums[i] + 1 != nums[i+1] :
                if longuest_sequence <= length :
                    longuest_sequence = length
                    length = 1
        
        return max(longuest_sequence,length)       
