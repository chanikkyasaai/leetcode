class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        for i in s:
            if i == '[':
                ans +=1
            elif ans >0:
                ans-=1
            
        return (ans+1)//2