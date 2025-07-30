class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0 
        j = k-1
        n = len(nums)
        sm = 0 
        for l in range(k):
            sm+= nums[l]

        maxavg = -float("inf")

        while j < n:
            maxavg = max(maxavg, sm/k)
            if j+1 < n:
                sm = sm - nums[i] + nums[j+1]
            i+=1
            j+=1
        return maxavg