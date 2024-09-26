class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = {0:1}
        cursum = 0
        count = 0

        for num in nums:
            cursum+= num

            if cursum - k in prefixsum:
                count+= prefixsum[cursum -k ]
            
            if cursum in prefixsum:
                prefixsum[cursum]+=1
            else:
                prefixsum[cursum] = 1
        
        return count