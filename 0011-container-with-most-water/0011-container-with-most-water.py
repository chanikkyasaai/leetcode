class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        area = (right - left)*min(height[left], height[right])

        while left< right:
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            area = max(area,(right - left)*min(height[left], height[right]))
        return area