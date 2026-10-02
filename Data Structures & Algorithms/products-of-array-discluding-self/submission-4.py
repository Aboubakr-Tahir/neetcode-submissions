class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0
        for ele in nums :
            if ele == 0 :
                count +=1 
            else : 
                product *= ele
        res = []
        if count >= 2 : 
            res = [0] * len(nums)
            return res
        else :
            for i , n in enumerate(nums) : 
                if count > 0 :
                    if n == 0 :
                        res.append(product)
                    else :
                        res.append(0)
                else : 
                    res.append(product // n)
        return res