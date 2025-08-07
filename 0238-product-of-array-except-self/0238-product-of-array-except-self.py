class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fwd = []
        fdp =  1
        for i in nums:
            fdp *= i
            fwd.append(fdp)
        bwd = []
        bdp = 1
        for i in reversed(nums):
            bdp*= i
            bwd.append(bdp)
        bwd.reverse()
        #1,2,6,24 -- 
        n = len(nums)
        res = [1]*n
        for i in range(n):
            if i-1>=0:
                res[i]*= fwd[i-1]
            if i+1 < n:
                res[i]*= bwd[i+1]
        
        return res

