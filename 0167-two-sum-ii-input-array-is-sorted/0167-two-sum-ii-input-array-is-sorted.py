class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        sm = numbers[left] + numbers[right]
        while sm != target:
            if sm >target:
                right-=1
            else:
                left+=1

            sm = numbers[left] + numbers[right]
        
        return [left+1, right+1]