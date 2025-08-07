class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            if i in seen:
                seen.remove(i)
            else:
                seen.add(i)
        
        return list(seen)[0]