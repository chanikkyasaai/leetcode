class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        initial = sum(nums[:k])
        maxsum = initial
        for i in range(k, len(nums)):
            initial += nums[i] - nums[i-k]
            maxsum = max(maxsum, initial)
        
        return maxsum/k