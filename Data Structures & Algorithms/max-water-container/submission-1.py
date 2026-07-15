class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_surface = 0
        while l < r :
            height = min(heights[l],heights[r])
            width = r-l
            curr_surface = height * width
            max_surface = max(max_surface,curr_surface)
            if heights[l] < heights[r] :
                l+=1 
            else :
                r-=1
        return max_surface