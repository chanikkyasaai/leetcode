from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        m = len(nums)
        left = 0
        win = set()
        maxsum = 0
        cursum = 0

        for right in range(m):
            while nums[right] in win:
                win.remove(nums[left])
                cursum-=nums[left]
                left+=1
            
            win.add(nums[right])
            cursum += nums[right]
            
            if right-left+1 == k:
                maxsum = max(maxsum, cursum)
                win.remove(nums[left])
                cursum-=nums[left]
                left+=1
        return maxsum
