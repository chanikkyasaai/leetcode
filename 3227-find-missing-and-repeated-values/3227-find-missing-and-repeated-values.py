class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = list(chain.from_iterable(grid))
        ans = [0,0]
        ind = [1] * len(arr)

        for i in arr:
            if ind[i-1] == 0:
                ans[0] = i
                continue
            ind[i-1] = 0
        
        ans[1] = ind.index(1) + 1
        
        return ans
