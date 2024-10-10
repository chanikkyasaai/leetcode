class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        maxwid = 0
        wid = []

        for i in range(n):
            if not wid or nums[i] < nums[wid[-1]]:
                wid.append(i)

        for j in range(n-1,-1,-1):
            while wid and nums[j] >= nums[wid[-1]]:
                maxwid = max(maxwid,j-wid.pop())
        
        return maxwid 