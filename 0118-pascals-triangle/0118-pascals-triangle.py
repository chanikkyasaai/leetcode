class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows ==1:
            return [[1]]

        ans = [[1], [1,1]]
        prev = ans[-1]
        for j in range(3,numRows+1):
            cur = [0]*(j)
            cur[0] = 1
            cur[-1] = 1
            for i in range(j-2):
                cur[i+1] = prev[i] + prev[i+1]
            
            prev = cur
            ans.append(cur)
        return ans

