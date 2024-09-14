class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        # mx = max(nums)

        # maxlen = 0
        # curlen = 0

        # for i in range(len(nums)):
        #     if nums[i] == mx:
        #         curlen +=1
        #         maxlen = max(maxlen, curlen)
        #     else:
        #         curlen = 0

        maxval = float('-inf')
        curlen = 0
        maxlen = 0

        for num in nums:
            if num > maxval:
                maxval =  num
                curlen =1
                maxlen = 1
            elif num == maxval:
                curlen +=1
                maxlen = max(maxlen, curlen)
            else:
                curlen = 0

        return maxlen
