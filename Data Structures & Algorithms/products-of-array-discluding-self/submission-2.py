class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for j,num_1 in enumerate(nums) :
            product = 1
            for i,num_2 in enumerate(nums) :
                if i == j and num_1 == num_2 : 
                    continue 
                product *= num_2

            res.append(product)
        return res