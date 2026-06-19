class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, num in enumerate(nums):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                # FIX: Recalculate the sum INSIDE the loop as pointers move
                threesome = num + nums[l] + nums[r]
                
                if threesome == 0:
                    res.append([num, nums[l], nums[r]])
                    
                    # FIX: Move pointers forward first
                    l += 1
                    r -= 1
                    
                    # FIX: Skip duplicates for the second element safely
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif threesome < 0:
                    l += 1
                else:
                    r -= 1
                    
        return res
