class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right_products = [1] * n
        left_products = [1] * n

        for i in range(len(nums) - 2,-1,-1):
            right_products[i] = nums[i+1] * right_products[i+1]
        
        for i in range(1,len(nums)):
            left_products[i] = nums[i-1] * left_products[i-1]
        
        res = [1] * n

        for i in range(n):
            res[i] = right_products[i] * left_products[i]
        
        return res