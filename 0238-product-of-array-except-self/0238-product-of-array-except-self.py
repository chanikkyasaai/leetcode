class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prepro = 1
        pospro = 1
        res = [0]*n

        for i in range(n):
            res[i]= prepro
            prepro *= nums[i]

        for j in range(n-1,-1,-1):
            res[j]*= pospro
            pospro *=nums[j]

        return res