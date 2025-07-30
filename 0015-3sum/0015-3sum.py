class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        ans = []
        for i in range(l):
            if i>0 and nums[i-1]==nums[i]:
                continue
            if i>=l-1:
                break
            left = i+1
            right = l -1
            target = -nums[i]
    
            while left < right:
                sm = nums[left] + nums[right]
                if target == sm:
                    ans.append([nums[i],nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif sm < target:
                    left+=1
                else :
                    right-=1
        return ans