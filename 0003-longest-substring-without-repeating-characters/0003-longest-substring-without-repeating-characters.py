class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        char = set()
        i = 0

        for j in range(len(s)):
            while s[j] in char:
                char.remove(s[i])
                i+=1
            char.add(s[j])
            maxlen = max(maxlen, j-i+1)
        return maxlen

