class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areamax = 0
        l, r = 0, len(heights) - 1

        # anclar la altura mas grande
        while l < r:
            areamax = max((min(heights[l], heights[r]) * (r - l)), areamax)

            # mover la altura más chica
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        return areamax