class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int, mxBits = 32) -> int:
        
        def updateMask(num, incr, mask = 0):
            
            for bit in range(mxBits):
                if num & (1 << bit):  bitCtr[bit]+= incr
                if bitCtr[bit]:  mask |= 1 << bit

            return mask

            
        if k == 0 or max(nums) >= k: return 1
        
        leftPtr, ans, bitCtr = 0, inf, [0] * mxBits
 
        for rghtPtr in range(len(nums)):
            mask = updateMask(nums[rghtPtr], 1)

            while mask >= k:
                ans = min(ans, rghtPtr - leftPtr + 1)   
                mask = updateMask(nums[leftPtr], -1)
                leftPtr += 1

        return -1 if ans == inf else ans