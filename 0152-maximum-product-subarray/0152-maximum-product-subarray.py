class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pree = 1
        suff = 1
        maxpro = float('-inf')
        n = len(nums)

        for i in range(n):
            if pree == 0:
                pree = 1
            if suff == 0:
                suff = 1
            pree *= nums[i]
            suff *= nums[n-i-1]
            maxpro = max(maxpro, max(pree, suff))

        return maxpro