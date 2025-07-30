class Solution:
    def trap(self, height: List[int]) -> int:
        ln = len(height)

        maxleft = [0]*ln
        maxl = -float("inf")
        maxleft[0] = height[0]
        for i in range(1,ln):
            maxleft[i] = max(height[i],maxleft[i-1])

        maxright = [0]*ln
        maxr = -float("inf")
        maxright[ln-1] = height[ln-1]
        for i in range(ln-2, -1, -1):
            maxright[i] = max(height[i], maxright[i+1])

        totalwater = 0
        for i in range(ln):
            wat = min(maxleft[i], maxright[i]) - height[i]
            if wat >0:
                totalwater+= wat
        return totalwater


