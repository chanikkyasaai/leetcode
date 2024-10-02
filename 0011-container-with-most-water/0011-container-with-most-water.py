class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n -1
        def maxvol(x,y):
            return (y - x)*min(height[x], height[y])
        
        maxivol = maxvol(i,j)
            
        while i < j:
            if height[i] < height[j]:
                i+=1
                maxivol = max(maxivol, maxvol(i,j))
            else:
                j-=1
                maxivol = max(maxivol, maxvol(i,j))
        
        return maxivol

