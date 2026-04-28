class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        start, end = 0, len(heights) - 1
        while start < end:
            width = end - start
            curr_height = min(heights[start], heights[end])
            area = width * curr_height
            maxarea = max(maxarea, area)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return maxarea
