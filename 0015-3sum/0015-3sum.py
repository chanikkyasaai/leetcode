class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)

        if nums.count(0) == n:
            return [[0,0,0]]

        for i in range(n):

            target = -nums[i]
            key_dict = { }

            for j in range(i+1,n):
                complement = target - nums[j]
                if complement in key_dict:
                        ls = (nums[i], nums[j], complement)
                        ans.add(tuple(sorted(ls)))

                key_dict[nums[j]] = j

        return ans