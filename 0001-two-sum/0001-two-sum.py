class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            comp = target - nums[i]
            
            if comp in nums:
                ind_comp = nums.index(comp)
                if ind_comp != i:
                    return [i, ind_comp]
                 