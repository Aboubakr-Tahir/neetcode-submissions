class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 :
            return []
        nums.sort()
        res = []
        for i in range(len(nums)) :
            if i == len(nums) - 1 :
                break
            if nums[i] == nums[i-1] and i-1 > 0 :
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r :
                sum_index = nums[i] + nums[l] + nums[r]
                if sum_index == 0 :
                    res.append([nums[i],nums[l] ,nums[r]])
                    l+= 1
                    r-= 1
                    while l < r and nums[l] == nums[l-1] :
                        l +=1
                if sum_index > 0 :
                    r-= 1
                    continue 
                if sum_index < 0 :
                    l += 1
                    continue
        hash_set = set()
        for arr in res :
            hash_set.add(tuple(arr))
        res = []
        for arr in hash_set :
            res.append(list(arr))
        return res 