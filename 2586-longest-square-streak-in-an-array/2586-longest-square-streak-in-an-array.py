class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        lgsqst = -1
        for i in nums:
            n = pow(i,2)
            ln = 1
            while n in nums:
                ln+=1
                n = pow(n,2)
            if ln != 1:
                lgsqst = max(ln,lgsqst)
        
        return lgsqst
            
