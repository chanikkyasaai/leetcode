class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lis = [1]*  len(nums)
        for i in nums:
            if lis[i-1] == 0:
                return i
            else:
                lis[i-1] =0