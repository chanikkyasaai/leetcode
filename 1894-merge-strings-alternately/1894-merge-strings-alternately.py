class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        m = len(word1)
        n = len(word2)

        for i in range(max(m,n)):
            if i < m:
                ans += word1[i]
            if i < n:
                ans += word2[i]
        
        return ans