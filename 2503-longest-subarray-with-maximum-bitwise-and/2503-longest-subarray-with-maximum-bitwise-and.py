class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        mx = max(nums)

        maxlen = 0
        curlen = 0

        for i in range(len(nums)):
            if nums[i] == mx:
                curlen +=1
                maxlen = max(maxlen, curlen)
            else:
                curlen = 0

        return maxlen
