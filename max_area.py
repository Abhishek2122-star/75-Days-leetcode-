# 11. Container With Most Water

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate area
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            
            # Move the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

