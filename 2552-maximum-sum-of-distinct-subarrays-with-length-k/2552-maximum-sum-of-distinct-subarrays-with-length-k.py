class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i, j, curS, maxS = 0, 0, 0, 0
        num_set = set()
        
        while j < len(nums):
            while nums[j] in num_set:
                num_set.remove(nums[i])
                curS -= nums[i]
                i += 1
                
            num_set.add(nums[j])
            curS += nums[j]
            
            if j - i + 1 == k:
                maxS = max(maxS, curS)
                num_set.remove(nums[i])
                curS -= nums[i]
                i += 1
            j += 1
        
        return maxS