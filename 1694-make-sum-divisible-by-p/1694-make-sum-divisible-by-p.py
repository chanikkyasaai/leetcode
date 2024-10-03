class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        subrem = sum(nums)%p

        if subrem == 0:
            return 0

        presum = 0
        minlen = float('inf')
        rem_dict = {0:-1}

        for i,num in enumerate(nums):
            presum = (presum + num) % p
            rem = (presum - subrem) % p

            if rem in rem_dict:
                minlen = min(minlen,i - rem_dict[rem])
            
            rem_dict[presum] = i

        return minlen if minlen != len(nums) else -1

            