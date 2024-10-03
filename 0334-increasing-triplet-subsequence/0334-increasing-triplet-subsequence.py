class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min0 = float('inf')
        min1 = float('inf')

        for num in nums:
            if num < min0:
                min0 = num
            elif num > min0:
                min1 = min(min1,num)
            if num > min1:
                return True
        
        return False