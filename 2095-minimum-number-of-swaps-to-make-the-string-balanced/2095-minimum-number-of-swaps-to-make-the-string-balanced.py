class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        balance = 0
        swaps = 0
        j = n - 1
        
        for i in range(n):
            if s[i] == '[':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                while s[j] != '[':
                    j -= 1
                balance += 2
                swaps += 1
                j -= 1  
        
        return swaps