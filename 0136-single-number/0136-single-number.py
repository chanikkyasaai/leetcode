class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         seen.remove(i)
        #     else:
        #         seen.add(i)
        
        # return list(seen)[0]

        nums.sort()
        i= 0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                i+=2
            else:
                return nums[i]
        return nums[i]