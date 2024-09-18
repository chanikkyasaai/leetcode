class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))

        def comparator(x,y):
            if x+y > y+x:
                return -1
            else :
                return 1
        
        nums.sort(key=cmp_to_key(comparator))
        result = ''.join(nums)

        return '0' if result[0] == '0' else result