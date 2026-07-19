class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        middle = (end + start) // 2
        while start <= end : 
            if nums[middle] == target :
                return middle
            elif nums[middle] > target :
                end = middle - 1
                middle = (end + start) // 2
            elif nums[middle] < target : 
                start = middle + 1
                middle = (end + start) // 2
        return -1
