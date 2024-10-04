class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen = 0
        noz = 0
        i = 0
        j = 0

        while j < len(nums):
            if nums[j] == 0:
                noz+=1
            while noz > k:
                if nums[i] == 0:
                    noz-=1
                i+=1
            maxlen = max(maxlen, j-i+1)
            j+=1

        return maxlen
                



