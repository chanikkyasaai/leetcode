class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        count = 0
        i = 0
        j = 0
        ans = ""
        
        while j < n:
            count = 0
            while j < n and word[i] == word[j] and count < 9:
                j += 1
                count += 1
            ans += str(count) + word[i]
            i = j
        
        return ans