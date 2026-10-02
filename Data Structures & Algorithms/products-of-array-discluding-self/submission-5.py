class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * length
        prefix = [0] * length
        suffix = [0] * length

        prefix[0] = 1
        suffix[length - 1] = 1

        for i in range(1,length) : 
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(length - 2 , -1 , -1) :
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(length) :
            res[i] = prefix[i] * suffix[i]
        
        return res