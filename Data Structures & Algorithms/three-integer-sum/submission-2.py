class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,num in enumerate(nums):
            if i > 0 and nums[i-1]==num :
                continue
            r=len(nums) - 1
            l= i+1
            while l<r :
                threesum = nums[i] + nums[l] + nums[r]
                if threesum == 0 :
                    res.append([nums[i],nums[r],nums[l]])
                    l+=1
                    r-=1
                    while l<r:
                        if nums[l] == nums[l-1] :
                            l+=1
                        else :
                            break
                elif threesum < 0 :
                    l +=1
                else :
                    r-=1
        return res