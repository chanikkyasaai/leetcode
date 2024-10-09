class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:         
        n = len(temperatures)
        ans = [0]*n
        stack = []
        for i in range(n):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                ans[j] = i-j
            stack.append(i)
        return ans