class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_surf = 0
        l = 0
        r = len(heights) - 1

        while l<r :
            curr_suf = (r-l) * min(heights[r],heights[l])
            if max_surf < curr_suf :
                max_surf=curr_suf
            elif heights[l] < heights[r] :
                l+=1
            elif heights[l] >= heights[r] :
                r -= 1
        return max_surf