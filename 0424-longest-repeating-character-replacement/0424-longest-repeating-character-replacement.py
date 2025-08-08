class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <=1:
            return len(s)
        charcount = [0]*26
        i=0
        charcount[ord(s[0]) - ord('A')] += 1
        maxc = 0

        for j in range(1, len(s)):
            charcount[ord(s[j]) - ord('A')]+=1
            while j-i+1 - max(charcount)>k:
                charcount[ord(s[i]) - ord('A')]-=1
                i+=1
            maxc = max(maxc, j-i+1)
        return maxc
            