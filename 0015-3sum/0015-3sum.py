class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ans = set()
        # n = len(nums)

        # if nums.count(0) == n:
        #     return [[0,0,0]]

        # for i in range(n):

        #     target = -nums[i]
        #     key_dict = { }

        #     for j in range(i+1,n):
        #         complement = target - nums[j]
        #         if complement in key_dict:
        #                 ls = (nums[i], nums[j], complement)
        #                 ans.add(tuple(sorted(ls)))

        #         key_dict[nums[j]] = j

        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i >0 and nums[i] == nums[i-1]:
                continue

            j,k = i+1,n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    ans.append([nums[i],nums[j], nums[k]])
                    j+=1
                    k-=1

                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1

                elif total <0:
                    j+=1
                else:
                    k-=1  

        return ans