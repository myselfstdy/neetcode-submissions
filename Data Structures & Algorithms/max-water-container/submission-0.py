class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        maxi = 0
        while left < right:
            h = min(heights[left] ,heights[right])
            w = right - left 
            area = h * w
            maxi = max(maxi,area)
            if heights[left] <= heights[right]:
                left +=1
            else:
                right -=1
        return maxi