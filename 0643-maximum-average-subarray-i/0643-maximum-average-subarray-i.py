class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0 
        j = k-1
        n = len(nums)
        sm = sum(nums[:k])

        maxsum = -float("inf")

        while j < n:
            maxsum = max(maxsum, sm)
            if j+1 < n:
                sm = sm - nums[i] + nums[j+1]
            i+=1
            j+=1
        return maxsum/k